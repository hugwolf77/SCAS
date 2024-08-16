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

        # 가장 간단한 것은 varInfo 의 정보를 전적으로 신뢰하고, 변수 목록을 그대로 적용하는것. (파일간 컬럼명(변수명)이 항상 일치한다는 전제 신뢰)
        # 추후 UI interface 에서 select된 columns를 답아서 선택되도록 변경
        selectCol=list(self.varList.values.flatten())
        self.data = loadVar[selectCol]
        self.data.sort_index(inplace=True, ascending=True)
        with pd.ExcelWriter(self.savePath+self.mainFile) as writer:
            self.dataInfo.to_excel(writer, sheet_name='varInfo', index=True)
            self.data.to_excel(writer, sheet_name='variable', index=True)
        return self.data