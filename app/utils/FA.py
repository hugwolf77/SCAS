
# normal distribution test
from scipy.stats import shapiro, kstest
from statsmodels.stats.diagnostic import kstest_normal
from scipy.stats import probplot

# bartlett's, KMO test for factor analysis
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

# foctor analysisj
from factor_analyzer.factor_analyzer import FactorAnalyzer
from statsmodels.multivariate.factor import Factor


class EFA_tool:
    def __init__(self,df, scale=True, drop_Na=False) -> None:
        #data
        if drop_Na == True : self.input_df = df.dropna()
        else: self.input_df = df

        # scaling
        # self.scaler = StandardScaler()
        # self.scaled_df = scaler.fit_transform(df)
        self.mean = df.mean()
        self.std = df.std()
        scaled_df = (self.input_df-self.mean)/self.std

        if scale == True: self.data = scaled_df
        else: self.data = self.input_df

        # norm dist test
    def faVal_test(self):
        chi_square_value,p_value=calculate_bartlett_sphericity(self.data)
        print(f"chi_square_value : {chi_square_value}")
        print(f"p_value() :{p_value}")

        kmo, p_value = calculate_kmo(self.data)
        print(f"chi_square_value : {kmo}")
        print(f"p_value() :{p_value}")

    # init fa
    def faAnly(self,n_factors=None,
                    rotation=None,
                    method='ml', 
                    smc=True,
                    is_corr_matrix=False,
                    bounds=(0.005,1),
                    impute='median',
                    svd_method='randomized',
                    rotation_kwargs=None
                    ):
        fa = FactorAnalyzer(
                            n_factors=n_factors,
                            rotation=rotation,
                            method=method, 
                            use_smc=smc,
                            is_corr_matrix=is_corr_matrix,
                            bounds=bounds,
                            impute=impute,
                            svd_method=svd_method,
                            rotation_kwargs=rotation_kwargs
                            )
        fa_result =  fa.fit(self.input_df)
        return fa, fa_result

