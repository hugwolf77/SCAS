from dataloader import dataloader
from tTools import stationary

def setData(df):
    loader = dataloader(df)
    loader.load()

def stationary_check(df):
    stn = stationary(df)
    stn.diffCheck()

if __name__ == "__main__":
    df = '분석_데이터_목록.xlsx'
    setData(df)
    stationary_check(df)