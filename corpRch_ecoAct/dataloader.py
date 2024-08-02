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
            indir = self.dataInfo["filePath"][self.dataInfo["fileName"]==file].iloc[0]
            loadVar.append(pd.read_excel(self.data_src_dir+indir+"/"+file, index_col='date'))
        loadVar = pd.concat(loadVar,axis=1)
        if self.dataInfo['분류구릅'][self.dataInfo['fileName']==file].iloc[0] == '기업 연구개발 투자 인력 환경':
            self.data =  loadVar[['연구소수','연구원수(연)','석박비율(연)','전담부서수','연구원수(전)','석박비율(전)']]
        
        self.data.columns = self.varList.values
        self.data.sort_index(inplace=True, ascending=True)
        with pd.ExcelWriter(self.savePath+self.mainFile) as writer:
            self.dataInfo.to_excel(writer, sheet_name='varInfo')
            self.data.to_excel(writer, sheet_name='variable')
        return self.data