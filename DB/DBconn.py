import os
import logging
from dotenv import load_dotenv

import pandas as pd
from pandas import DataFrame
# import sqlite3
# import psycopg2 as pg2

from sqlalchemy import URL
from sqlalchemy import create_engine
# from sqlalchemy import sql
from sqlalchemy.orm import Session #, sessionmaker
# SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

# database table model
from dataModel.PJ01_TB_model import BASE, CORP_RCH_ECONOMIC

# logging
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p',) #filename="example.log"
logging.getLogger("sqlalchemy.engine.Engine.myengine")

# .env
load_dotenv()

class DW:
    def __init__(self) -> None:

        if os.getenv("DMBS") == 'postgresql+psycopg2':
            self.url_object = URL.create(
                                        os.getenv("DMBS"),
                                        username=os.getenv("User"),
                                        password=os.getenv("PW"),
                                        host=os.getenv("DB_URL"),
                                        database=os.getenv("DB"),
                                )
        else:
            self.url_object = f"sqlite:///{os.getcwd()+'/DB/DataBase/scas.db'}" 

        self.engine =  create_engine(self.url_object, echo=True, logging_name=os.getenv("LOG"))

    def _DB_INIT_TABLE_(self)->None:
        try:
            BASE.metadata.create_all(self.engine)
            print(f"Initialized The DataBase Tables")
        except:
            print(f"Failed to initialize The DataBase tables.")

    # 
    def _TABLE_INSERT_(self,table:str, value:list):
        with Session(self.engine) as session:
            Lvalue = [Item for Item in value]
            session.add_all(Lvalue)

    def _PD_read_(self,table:str)->DataFrame:
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query,con=self.engine)
        return df
   
    def _PD_to_(self,df:DataFrame,table:str,obtion:str='replace')->None:
        with self.engine.connect() as con:
            df.to_sql(
                name=table.upper(),
                con=con,
                if_exists=obtion
            )

if __name__== "__main__":
    print(f"pwd : {os.getcwd()}")
    print(f"sqlite:///{os.getcwd()+'/DB/DataBase/scas.db'}"  )
    df = pd.read_excel('./DB/Data/분석_데이터_목록_v2.xlsx', sheet_name='transData', index_col='date')
    dw = DW()
    dw._DB_INIT_TABLE_()
    dw._PD_to_(df,'CORP_RCH_ECONOMIC')