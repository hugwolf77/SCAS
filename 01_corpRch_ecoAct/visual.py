import matplotlib as mpl
import matplotlib.font_manager
import matplotlib.pyplot as plt
import seaborn as sns

font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
[matplotlib.font_manager.FontProperties(fname=font).get_name() for font in font_list if 'Nanum' in font]

plt.rc('font', family='NanumGothicCoding')
mpl.rcParams['axes.unicode_minus'] = False


def heatmap(df):
    plt.figure(figsize=(15,30))
    sns.heatmap(df.isna().transpose(),
                cmap="YlGnBu",
                cbar=False,
                # cbar_kws={'label': 'Missing Data'}
                )
    plt.show()