from dataloader import dataloader
from tTools import stationary

def main(df):
    # "분석_데이터_목록.xlsx"파일의 정보를 이용 데이터 기간 및 계절조정, 컬럼 확인된 원-엑셀파일로 부터 데이터 읽고 "분석_데이터_목록.xlsx"의 "varialb" sheet로 읽어 드림
    loader = dataloader(df)
    loader.load()
    # 분석_데이터_목록.xlsx"의 "varialb" sheet로 읽고, 정상성에 대한 4가지 상태(차분상태)를 체크하고 "diffCheck" sheet를 생성 저장
    stn = stationary(df)
    stn.diffCheck()
    stn.trans_data()


if __name__ == "__main__":
    df = '분석_데이터_목록_v2.xlsx'
    main(df)
