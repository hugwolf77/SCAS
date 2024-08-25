
# 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family='NanumBarunGothic') 
plt.rcParams['axes.unicode_minus'] =False

# scaler
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# normal distribution test
from scipy.stats import shapiro, kstest
from statsmodels.stats.diagnostic import kstest_normal
from scipy.stats import probplot

# bartlett's, KMO test for equel distribution
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

# foctor analysis
from factor_analyzer.factor_analyzer import FactorAnalyzer
from statsmodels.multivariate.factor import Factor


# data load
df = pd.read_excel('./data/분석_데이터_목록.xlsx', sheet_name='transData', index_col='date')

# scaling
# scaler = StandardScaler()
# scaled = scaler.fit_transform(df)
mean = df.mean()
std = df.std()
scaled = (df - mean)/std 

# plot
df_std = scaled.melt(var_name='Column', value_name='Normalized')
plt.figure(figsize=(12, 6))
ax = sns.violinplot(x='Column', y='Normalized', data=df_std)
_ = ax.set_xticklabels(df.keys(), rotation=90)
plt.show()


# drop couldn't use variable and check Nan data
data = scaled.drop('실업률', axis=1)
data = data.iloc[2:,:] 
# Nan
print(f"{data.isna().sum()}")
print(f"{data.isnull().sum()}")
plt.figure(figsize=(10,10))
sns.heatmap(data.isna())
plt.show()

print(data.head())
print(data.tail(10))

# norm dist test
chi_square_value,p_value=calculate_bartlett_sphericity(data)
print(f"chi_square_value : {chi_square_value}")
print(f"p_value() :{p_value}")

kmo, p_value = calculate_kmo(data)
print(f"chi_square_value : {kmo}")
print(f"p_value() :{p_value}")


# # init fa
# fa = FactorAnalyzer(n_factors=23, method='ml', rotation=None)
# fa.fit(data)
# print(fa.loadings_)

if __name__ == "__main__":
    pass
