import os
import numpy as np
import pandas as pd


class dataloader:
    def __init__(self, mainFile):
        self.mainFile = mainFile
        self.data_src_dir = os.path.join(os.getcwd(),'data/')
        self.dataInfo = pd.read_excel(self.data_src_dir+self.mainFile,sheet_name='varInfo',header=0, index_col='순서')
        self.dataFiles = list(set(self.dataInfo['fileName']))
        self.varList = self.dataInfo['변수명']
        self.data = pd.DataFrame()
        self.savePath = self.data_src_dir
    
    def load(self):
        loadVar = []
        for file in self.dataFiles:
            print(f"file loading --- : {file}")
            indir = list(self.dataInfo["filePath"][self.dataInfo["fileName"]==file].unique())[0]
            loadVar.append(pd.read_excel(self.data_src_dir+indir+"/"+file, index_col='date'))
        loadVar = pd.concat(loadVar,axis=1)

        for group in self.dataInfo['분류구릅'].unique():
            print(f"Data variable category group processing: {group}")
            if self.dataInfo['분류구릅'][self.dataInfo['fileName']==file].iloc[0] == group:
                self.data = pd.concat([self.data, loadVar[['연구소수','연구원수(연)','석박비율(연)','전담부서수','연구원수(전)','석박비율(전)']]], axis=1)
            if (self.dataInfo['분류구릅'][self.dataInfo['fileName']==file].iloc[0] == group) and (self.dataInfo['데이터 소속'][self.dataInfo['fileName']==file].iloc[0] == '경제 활동 역동성' or '경제 활동 인구구조'):
                self.data = pd.concat([self.data, loadVar[['경제활동인구','취업자','비임금근로자','고용원이 있는 자영업자','고용원이 없는 자영업자',
                                    '무급가족종사자','임금근로자','상용근로자','임시근로자','일용근로자','남자','여자',
                                    '실업자','실업률','15세이상인구','비경제활동인구','경제활동참가율','고용률',]]], axis=1)
            else:
                pass
        
        self.data.columns = self.varList.values
        self.data.sort_index(inplace=True, ascending=True)
        with pd.ExcelWriter(self.savePath+self.mainFile) as writer:
            self.dataInfo.to_excel(writer, sheet_name='varInfo', index=True)
            self.data.to_excel(writer, sheet_name='variable', index=True)
        return self.data