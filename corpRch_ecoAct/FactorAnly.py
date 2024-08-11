
# 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# normal distribution test
from scipy.stats import shapiro, kstest
from statsmodels.stats.diagnostic import kstest_normal
from scipy.stats import probplot

# bartlett's, KMO test for equel distribution
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

# foctor analysis
from factor_analyzer.factor_analyzer import FactorAnalyzer
from statsmodels.multivariate.factor import Factor

df = pd.read_excel('./data/분석_데이터_목록.xlsx', sheet_name='variable', index_col='date')

df.plot()
plt.show()
print(df.head())

df = df.values
chi_square_value,p_value=calculate_bartlett_sphericity(df)
print(f"chi_square_value : {chi_square_value}")
print(f"p_value() :{p_value}")

