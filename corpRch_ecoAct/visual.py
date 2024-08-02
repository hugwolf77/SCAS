import matplotlib.pyplot as plt
import seaborn as sns

def heatmap(df):
    plt.figure(figsize=(15,30))
    sns.heatmap(df.isna().transpose(),
                cmap="YlGnBu",
                cbar=False,
                # cbar_kws={'label': 'Missing Data'}
                )
    plt.show()