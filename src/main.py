from fastapi import FastAPI
from src.catboost import router as catboost_router
from src.rf import router as rf_router
from src.doc import router as doc_router

app = FastAPI(
    title="Income Prediction API",
    description="An API for predicting income levels using CatBoost and Random Forest models.",
    version="1.0.0"
)

# Include the routers 

app.include_router(catboost_router)  
app.include_router(rf_router)
app.include_router(doc_router)  
