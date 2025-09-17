from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware  # Import the CORSMiddleware
from helper.helper import Preprocess
from exception.exception import CustomException
import sys

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",  # Replace with the actual URL of your frontend
    "http://localhost:5500",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specifies the allowed origins
    allow_credentials=True, # Allows cookies and authentication headers
    allow_methods=["*"],    # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],    # Allows all headers
)

class InputData(BaseModel):
    question1: str
    question2: str

@app.get("/")
def index():
    return {"message": "Hii! welcome to my Duplicate question prediction. go to /predict"}

@app.post('/predict')
def predict(data: InputData):
    q1 = data.question1
    q2 = data.question2
    try:
        preproccess = Preprocess()
    except Exception as e:
        raise CustomException(e, sys)
    
    if q1 is not None and q2 is not None:
        try:
            temp = preproccess.query_point_creator(q1=q1, q2=q2)
            pred = preproccess.predict(temp)
        except Exception as e:
            raise CustomException(e, sys)
    return {"result": pred}