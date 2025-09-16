import os
import numpy as np
import pandas as pd
import sys
import json
from dotenv import load_dotenv
load_dotenv()
import pymongo
import certifi
ca = certifi.where()

from exception.exception import CustomException
from my_logging.logger import logging

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DuplicateQuestionData:
    def __init__(self):
        pass
    
    def csv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = json.loads(data.to_json(orient="records"))
            return records
        except Exception as e:
            raise CustomException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
            self.database = self.mongo_client[self.database]    # To access a database in MongoDB
            self.collection = self.database[self.collection]    # accesses the specific collection within the MongoDB database.

            self.collection.insert_many(self.records)
            logging.info("Data push successfuly in MongoDB")
            return len(self.records)
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__" :
    FILE_PATH = "Data/train.csv"
    DATABASE = "OnkarShinde"
    Collection = "Duplicate_Question_data"
    duplicate_question_data = DuplicateQuestionData()
    records = duplicate_question_data.csv_to_json(FILE_PATH)
    no_of_records = duplicate_question_data.insert_data_mongodb(records=records,database=DATABASE,collection=Collection)
    print(no_of_records)