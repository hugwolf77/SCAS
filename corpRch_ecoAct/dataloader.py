import os
import numpy as np
import pandas as pd


class dataloader:
    def __init__(self, mainFile):
        self.mainFile = mainFile
        self.data_src_dir = os.path.join(os.getcwd(),'data/')
        self.dataInfo = pd.read_excel(self.data_src_dir+self.mainFile,sheet_name='varInfo',header=0)
        self.dataFiles = list(set(self.dataInfo['fileName']))
        self.varList = self.dataInfo['변수명']
        self.data = pd.DataFrame()
        self.savePath = self.data_src_dir
    
    def load(self):
        loadVar = []
        for file in self.dataFiles:
            print(f"file : {file}")
            indir = list(self.dataInfo["filePath"][self.dataInfo["fileName"]==file].unique())[0]
            loadVar.append(pd.read_excel(self.data_src_dir+indir+"/"+file, index_col='date'))
        loadVar = pd.concat(loadVar,axis=1)

        # if 문 전에 분류 구릅에 따른 iter loop 후에 각 DataFrame을 넣은 list를 concat

        if self.dataInfo['분류구릅'][self.dataInfo['fileName']==file].iloc[0] == '기업 연구개발 투자 인력 환경':
            self.data =  loadVar[['연구소수','연구원수(연)','석박비율(연)','전담부서수','연구원수(전)','석박비율(전)']]
        if (self.dataInfo['분류구릅'][self.dataInfo['fileName']==file].iloc[0] == '경제_사회_인구구조') and (self.dataInfo['데이터 소속'][self.dataInfo['fileName']==file].iloc[0] == '경제 활동 역동성' or '경제 활동 인구구조'):
            self.data =  loadVar[['경제활동인구','취업자','비임금근로자','고용원이 있는 자영업자','고용원이 없는 자영업자',
                                  '무급가족종사자','임금근로자','상용근로자','임시근로자','일용근로자','남자','여자',
                                  '실업자','실업률','15세이상인구','비경제활동인구','경제활동참가율','고용률',]]
        
        self.data.columns = self.varList.values
        self.data.sort_index(inplace=True, ascending=True)
        with pd.ExcelWriter(self.savePath+self.mainFile) as writer:
            self.dataInfo.to_excel(writer, sheet_name='varInfo')
            self.data.to_excel(writer, sheet_name='variable')
        return self.data