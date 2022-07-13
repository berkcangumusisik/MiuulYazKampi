# 5. Korelasyon Analizi (Analysis of Correlation)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
print(df.head())

numCols = [col for col in df.columns if df[col].dtype in [int, float]]
print(numCols)

corr = df[numCols].corr()  # korelasyon matrisi oluşturma
print(corr)
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

# Yüksek Korelasyonlu Değişkenlerin Silinmesi
#######################

corMatrix = df.corr().abs()

#           0         1         2         3
# 0  1.000000  0.117570  0.871754  0.817941
# 1  0.117570  1.000000  0.428440  0.366126
# 2  0.871754  0.428440  1.000000  0.962865
# 3  0.817941  0.366126  0.962865  1.000000


#     0        1         2         3
# 0 NaN  0.11757  0.871754  0.817941
# 1 NaN      NaN  0.428440  0.366126
# 2 NaN      NaN       NaN  0.962865
# 3 NaN      NaN       NaN       NaN

upperTriangleMatrix = corMatrix.where(np.triu(np.ones(corMatrix.shape), k=1).astype(bool))
drop_list = [col for col in upperTriangleMatrix.columns if any(upperTriangleMatrix[col]>0.90) ]
corMatrix[drop_list]
df.drop(drop_list, axis=1)
print(df.head())

def highCorrelatedCols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    corMatrix = corr.abs()
    upperTriangleMatrix = corMatrix.where(np.triu(np.ones(corMatrix.shape), k=1).astype(bool))
    dropList = [col for col in upperTriangleMatrix.columns if any(upperTriangleMatrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return dropList

highCorrelatedCols(df)
drop_list = highCorrelatedCols(df, plot=True)
df.drop(drop_list, axis=1)
highCorrelatedCols(df.drop(drop_list, axis=1), plot=True)

# Yaklaşık 600 mb'lık 300'den fazla değişkenin olduğu bir veri setinde deneyelim.
# https://www.kaggle.com/c/ieee-fraud-detection/data?select=train_transaction.csv

df = pd.read_csv("datasets/fraud_train_transaction.csv")
print(len(df.columns))
print(df.head())

drop_list = highCorrelatedCols(df, plot=True)

print(len(df.drop(drop_list, axis=1).columns))