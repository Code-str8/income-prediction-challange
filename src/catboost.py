from fastapi import APIRouter
from pydantic import BaseModel,conint,ValidationError
from typing import Optional
import pandas as pd
import joblib

#load the model&encoder
catboost_model = joblib.load('models/catboost_pipeline_thresh.pkl')
le = joblib.load('models/LabelEncoder.pkl')

class InputData(BaseModel):
    age: conint(ge=0)
    gender: str
    education: str
    work_class: Optional[str] = None
    marital_status: str
    race: str
    is_hispanic: str
    employment_stat: conint(ge=0)
    wage_per_hour: conint(ge=0)
    working_week_per_year: conint(ge=0)
    industry_code: conint(ge=0)
    occupation_code: conint(ge=0)
    total_employed: conint(ge=0)
    household_summary: str
    tax_status: str
    gains: conint(ge=0)
    losses: conint(ge=0)
    stocks_status: conint(ge=0)
    citizenship: str
    mig_year: conint(ge=0)
    importance_of_record: float

    @classmethod
    def validate_gender(cls, value):
        if value not in ['m', 'f']:
            raise ValueError("Gender should be either 'm' or 'f'")
        return value

    @classmethod
    def validate_is_hispanic(cls, value):
        if value not in ['0', '1']:
            raise ValueError("is_hispanic should be either '0' or '1'")
        return value

    @classmethod
    def validate(cls, values):
        errors = []
        try:
            values['gender'] = cls.validate_gender(values['gender'])
        except ValueError as e:
            errors.append(e)

        try:
            values['is_hispanic'] = cls.validate_is_hispanic(values['is_hispanic'])
        except ValueError as e:
            errors.append(e)

        if errors:
            raise ValidationError(errors)

        return values



# Create a dictionary mapping column names to data types
col_dtypes = {
    'age': 'int64',
    'gender': 'category',
    'education': 'category',
    'work_class': 'category',
    'marital_status': 'category',
    'race': 'category',
    'is_hispanic': 'category',
    'employment_stat': 'int64',
    'wage_per_hour': 'int64',
    'working_week_per_year': 'int64',
    'industry_code': 'int64',
    'occupation_code': 'int64',
    'total_employed': 'int64',
    'household_summary': 'category',
    'tax_status': 'category',
    'gains': 'int64',
    'losses': 'int64',
    'stocks_status': 'int64',
    'citizenship': 'category',
    'mig_year': 'int64',
    'importance_of_record': 'float64'
}


# a router for the catboost endpoint
router = APIRouter(
    prefix="/Catboost",
    tags=["Catboost Model"]
)
@router.post("/prediction")
async def cat_predict(col: InputData):
          cols = list(col.dict().keys())
          data = list(col.dict().values())
          df = pd.DataFrame([data], columns=cols)
          df = df.astype(col_dtypes)

          # make prediction
          pred_proba = catboost_model.predict_proba(df)

          pred = catboost_model.predict(df)
          
          pred = le.inverse_transform(pred) 

          prob = pred_proba.max()*100

          prob = "{:.1f}%".format(prob) 

          return {"prediction":pred[0],"probability":prob}
