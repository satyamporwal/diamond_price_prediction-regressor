import os
import sys 
from src.logger import logging
from src.exception import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import Datatransformation



#intializing step 1 for data ingestion
@dataclass
class DataIngestionconfig:
    train_data_path = os.path.join('artifacts',train.csv)
    test_data_path = os.path.join('artifacts',test.csv)
    raw_data_path = os.path.join('artifacts',raw.csv)

class Dataingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()
    
    def initiate_dataingestion(self):
        logging.info("ingestion started")
        try:
            df = pd.read_csv(os.path.join("https://raw.githubusercontent.com/krishnaik06/FSDSRegression/main/notebooks/data/gemstone.csv"))
            logging.info('reading csv file')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            logging.info("makeing dir before train test spilt")

            train_set,test_set = train_test_split(df,test_size=0.30,random_state=50)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('data seprtaed in to train & test data & data ingestion is done in artifacts')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
    
        except Exception as e:
            logging.info('there is problem in data ingestion')
            raise CustomException(e,sys)
        


if __name__ == '__main__':
    obj = Dataingestion()
    train_data,test_data = obj.initiate_dataingestion()
        

