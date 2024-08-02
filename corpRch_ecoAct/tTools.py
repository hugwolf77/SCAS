# base
import os

# 데이터 로딩 및 조작을 위한 라이브러리
import pandas as pd
import numpy as np

# 정상성 테스트를 위한 라이브러리
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
# 시계열 분해
from statsmodels.tsa.seasonal import seasonal_decompose

def remove_outliers(dta):
    # Compute the mean and interquartile range
    mean = dta.mean()
    iqr = dta.quantile([0.25, 0.75]).diff().T.iloc[1]
    # Replace entries that are more than 10 times the IQR
    # away from the mean with NaN (denotes a missing entry)
    mask = np.abs(dta) > mean + 10 * iqr
    treated = dta.copy()
    treated[mask] = np.nan
    return treated

def adf_test(timeseries):
    ## perform augmented dickey fuller test
    print('Results of Augmented Dickey-Fuller test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['test statistic','p-value','# of lag','# of observations'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value ({})'.format(key)] = value
    return (dfoutput)

def kpss_test(timeseries):
    print("Results of KPSS Test:")
    kpsstest = kpss(timeseries, regression="c", nlags="auto")
    kpss_output = pd.Series(
        kpsstest[0:3], index=["Test Statistic", "p-value", "Lags Used"] )

    for key, value in kpsstest[3].items():
        kpss_output["Critical Value (%s)" % key] = value
    print(kpss_output)


class stationary:
    def __init__(self, mainFile, start=None, end=None):
        self.mainFile = mainFile
        self.path = os.path.join(os.getcwd()+"/data",mainFile)
        self.df = pd.read_excel(self.path,sheet_name='variable',header=0)
        self.varInfo = pd.read_excel(self.path,sheet_name='varInfo',header=0)
        self.varList = self.varInfo['변수명']
        self.savePath = self.path
        self.setDiff = ['Origin','Diff-1','Log-1','Diff-2']
        self.start = start
        self.end = end
        self._test_result = pd.DataFrame()

    def testStatationary(self, transformed):
        if (result := adfuller(transformed.values))[1] < 0.05 :
            test_result = "{}".format("S")
        else:
            test_result = "{}".format("N")
        return test_result

    def diffCheck(self):
        i = 0
        list_test_result = []
        for var in self.varList:
            for t in self.setDiff:
                i += 1
                print(f"processing....{i}.... [ {var} ------{t}--test--- ]")
                # test
                if t == 'Origin':
                    transformed = self.df[var].dropna()
                    res = self.testStatationary(transformed)
                elif t == 'Diff-1':
                    transformed = self.df[var].diff().dropna()
                    res = self.testStatationary(transformed)
                elif t == 'Log-1':
                    log_1 = self.df[var]
                    transformed = np.log(log_1).dropna()
                    res = self.testStatationary(transformed)
                elif t == 'Diff-2':
                    transformed = self.df[var].diff().diff().dropna()
                    res = self.testStatationary(transformed)
                else:
                    pass

                g = self.varInfo['분류구릅'][self.varInfo['변수명']==var].values
                # print(type(g[0]))
                # raise
                _result = [g[0],var,t,res]
                list_test_result.append(_result)
        
        self._test_result = pd.DataFrame(list_test_result,columns = ['group','variable','transform','adf'] )
        self._test_result = self._test_result.pivot(index= ['group','variable'], columns='transform', values='adf')
        with pd.ExcelWriter(self.savePath) as writer:
            self.varInfo.to_excel(writer, sheet_name='varInfo')
            self.df.to_excel(writer, sheet_name='variable')
            self._test_result.to_excel(writer, sheet_name='diffCheck')
        # self._test_result.to_excel(self.savePath, sheet_name='diffCheck')
