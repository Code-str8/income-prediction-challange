from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel
from typing import Optional, Literal

app = FastAPI(
    title="Income Prediction API",
    description="An API for predicting income levels using CatBoost and Random Forest models.",
    version="1.0.0"
)

# Load the required features and models
with open('models/LabelEncoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

with open('models/catboost_pipeline_thresh.pkl', 'rb') as f:
    cat_pipeline = pickle.load(f)

with open('models/rf_pipeline_thresh.pkl', 'rb') as f:
    rf_pipeline = pickle.load(f)

# Define the input data structure
class InputData(BaseModel):
    age: int
    gender: str
    education: str
    work_class: Optional[str] = None
    marital_status: str
    race: str
    is_hispanic: str
    employment_stat: int
    wage_per_hour: int
    working_week_per_year: int
    industry_code: int
    occupation_code: int
    total_employed: int
    household_summary: str
    tax_status: str
    gains: int
    losses: int
    stocks_status: int
    citizenship: str
    mig_year: int
    importance_of_record: float

# Define the prediction function
def predict_income(data):
    # Preprocess the input data
    data_df = pd.DataFrame([data.dict()])
    X = data_df.drop('importance_of_record', axis=1)
    X = encoder.transform(X)
    
    # Make predictions using both models
    cat_pred = cat_pipeline.predict(X)[0]
    rf_pred = rf_pipeline.predict(X)[0]
    
    # Map predictions to 'Above Limit' and 'Below Limit'
    cat_pred = 'Above Limit' if cat_pred == 1 else 'Below Limit'
    rf_pred = 'Above Limit' if rf_pred == 1 else 'Below Limit'
    
    return {'catboost_prediction': cat_pred, 'random_forest_prediction': rf_pred}

# Define the API endpoint
@app.post('/predict', tags=["Prediction"], response_model=dict)
def predict(data: InputData):
    try:
        prediction = predict_income(data)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/", tags=["Health Check"])
def health_check():
    return {"message": "Income Prediction API is running"}

# Documentation endpoint
@app.get("/docs", tags=["Documentation"], include_in_schema=False)
def docs():
    return RedirectResponse(url="/docs")
