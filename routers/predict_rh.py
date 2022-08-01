from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder, defaultdict
from pydantic import BaseModel
from services.predict_rh import PredictRH

import json


router = APIRouter(prefix='/ibm', responses={404: {'descriptios': 'not found'}})


class RequestBodyData(BaseModel):
    Age: int
    BusinessTravel: str
    DailyRate: int
    Department: str
    DistanceFromHome: int
    Education: int
    EducationField: str
    EnvironmentSatisfaction: int
    Gender: str
    HourlyRate: int
    JobInvolvement: int
    JobLevel: int
    JobRole: str
    JobSatisfaction: int
    MaritalStatus: str
    MonthlyIncome: int
    MonthlyRate: int
    NumCompaniesWorked: int
    OverTime: str
    PercentSalaryHike: int
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int




@router.post('/')
async def predict(request: RequestBodyData):
    result = PredictRH().predict(request.json())
    return result


@router.post('/teste')
async def predict_teste(request: RequestBodyData):
    result = PredictRH().teste(request.json())
    return result