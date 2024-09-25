
import os

import numpy as np
import pandas as pd

import statsmodels.api as sm
import statsmodels.stats as sm_stat
import statsmodels.tsa as smt
import statsmodels.formula.api as smf

from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.seasonal import seasonal_decompose

import scipy
import matplotlib.pyplot as plt


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


class LinearModel:
    def __init__(self, data) -> None:
        self.data = data
        self.result = dict()
        self.sMean = data.mean(axis=0)
        self.sVar = data.var(axis=0)

    #Lag operator:
    def Lag(self, x, n=1):
        if n ==0:
            return x 
        if isinstance(x, pd.Series):
            return x.shift(n)
        else:
            x = pd.Series(x)
            return x.shift(n)
        
    #Difference operator:  << switching or depreacate
    def d(self, x):
        if isinstance(x, pd.Series):
            return x.diff()
        else:
            x = pd.Series(x)
            return x.diff()

    #Trend/time operator:
    def seq(self, x):
        return list(range(1, len(x)+1))
    
    # the null hypothesis : variable (the series) is a zero-mean
    def zeroMean(self):
        scipy.stats.ttest_lsmp(self.data, popmean = 0)

    def fomula_model(self, formula:str, data, mtype='unrestrict'):
        model = smf.ols(formula=formula, data=self.data).fit()
        fitOut = self.get_coef(model)
        self.result[mtype] = fitOut
        return self.result[mtype]

    def get_coef(self, mdl_fit):
        result = np.round(pd.DataFrame([mdl_fit.params, mdl_fit.tvalues, mdl_fit.pvalues], index = ["coef","t-value","p-value"]).T, 5)
        return result
    
    def compareModel(self):
         sm_stat.api.anova_lm(self.result['unrestrict'], )



class stationary:
    def __init__(self, mainFile, start=None, end=None):
        self.mainFile = mainFile
        self.path = os.path.join(os.getcwd()+"/data",mainFile)
        self.df = pd.read_excel(self.path,sheet_name='variable',header=0, index_col='date')
        self.varInfo = pd.read_excel(self.path,sheet_name='varInfo',header=0, index_col='순서')
        self.varList = self.varInfo['변수명']
        self.savePath = self.path
        self.setDiff = ['Origin','Diff-1','Log-1','Diff-2']
        self.start = start
        self.end = end
        self._test_result = pd.DataFrame()

    def testStatationary(self, transformed):
        try:
            if (result := adfuller(transformed.values))[1] < 0.05 :
                test_result = "{}".format("S")
            else:
                test_result = "{}".format("N")
            return test_result
        except ZeroDivisionError as e:
            print(f"{transformed.name} : ZeroDivisionError  : {e}")
        except IndexError as e:
            print(f"{transformed.name} : IndexError  : {e}")
        except :
            print(f"{transformed.name} : Error ")

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
                elif t == 'Diff-1':
                    transformed = self.df[var].diff().dropna()
                elif t == 'Log-1':
                    log_1 = self.df[var]
                    transformed = np.log(log_1).dropna()
                elif t == 'Diff-2':
                    transformed = self.df[var].diff().diff().dropna()
                else:
                    pass
                res = self.testStatationary(transformed)
                g = self.varInfo['분류구릅'][self.varInfo['변수명']==var].values
                # print(type(g[0]))
                # raise
                _result = [g[0],var,t,res]
                list_test_result.append(_result)
        self._test_result = pd.DataFrame(list_test_result,columns = ['group','variable','transform','adf'] )
        self._test_result = self._test_result.pivot(index= ['group','variable'], columns='transform', values='adf')


        with pd.ExcelWriter(self.savePath) as writer:
            self.varInfo.to_excel(writer, sheet_name='varInfo', index=True)
            self.df.to_excel(writer, sheet_name='variable', index=True)
            self._test_result.to_excel(writer, sheet_name='diffCheck', index=True)
        # self._test_result.to_excel(self.savePath, sheet_name='diffCheck')

    def trans_data(self):
        transformed_result = []

        for var in self.varList:
            t  = self.varInfo['Diff'][self.varInfo['변수명']==var].values
            print(f"processing..... [ {var} ------Diff : {t} --trans--- ]")
            # raise
            # test
            if t == 'Origin':
                transformed = self.df[var].dropna()
            elif t == 'Diff-1':
                transformed = self.df[var].diff().dropna()
            elif t == 'Log-1':
                log_1 = self.df[var]
                transformed = np.log(log_1).dropna()
            elif t == 'Diff-2':
                transformed = self.df[var].diff().diff().dropna()
            else:
                transformed = self.df[var].dropna()

            transformed_result.append(transformed)
        diff_variable = pd.DataFrame(transformed_result).T #, index=self.df.index)
        # print(diff_variable.index)
        self.varInfo = pd.read_excel(self.path,sheet_name='varInfo',header=0, index_col='순서')
        self.df = pd.read_excel(self.path,sheet_name='variable',header=0, index_col='date')
        self._test_result = pd.read_excel(self.path,sheet_name='diffCheck', header=0)

        with pd.ExcelWriter(self.savePath) as writer:
            self.varInfo.to_excel(writer, sheet_name='varInfo', index=True)
            self.df.to_excel(writer, sheet_name='variable', index=True)
            self._test_result.to_excel(writer, sheet_name='diffCheck', index=True)
            diff_variable.to_excel(writer, sheet_name='transData', index=True)

if __name__ == "__main__":
    pass
