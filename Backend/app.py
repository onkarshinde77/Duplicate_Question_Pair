from fastapi import FastAPI
from pydantic import BaseModel
from helper.helper import Preprocess
from exception.exception import CustomException
import sys


app = FastAPI()

class InputData(BaseModel):
    question1: str
    question2: str

@app.get("/")   # <- fixed
def index():
    return {"message": "Hii! wwelcome my Duplicate question prediction. go /predict"}  

@app.post('/predict')
def predict(data:InputData):
    q1 = data.question1
    q2 = data.question2
    try:
        preproccess = Preprocess()
    except Exception as e:
        raise CustomException(e,sys)
    
    if q1 is not None and q2 is not None:
        try:
            temp = preproccess.query_point_creator(q1=q1,q2=q2)
            pred = preproccess.predict(temp)
        except Exception as e:
            raise CustomException(e,sys)
    
    return {"result": pred}