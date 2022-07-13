# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/advertising.csv")
df = sns.load_dataset("titanic")
print(df.head())

catCols = [col for col in df.columns if str(df[col].dtype) in ['object', 'category', "bool"]]
print(catCols)  # Tip olarak object, category veya bool olan sütunların listesi

numButCat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
# Tip olarak int veya float olan sütunların listesi ve 10'dan küçük nunique değerleri olan sütunların listesis
print(numButCat)

catButCar = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

# Tip olarak category veya object olan ve 20'den büyük eşsiz sınıf sayısı  olan sütunların listesi
print(catButCar)
catCols = catCols + numButCat
print(catCols)

catCols = [col for col in catCols if col not in catButCar]
print(catCols)
numCols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
print(numCols)
numCols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
numCols = [col for col in numCols if col not in catCols]
print(numCols)


def numSummary(dataframe, numericalCol):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numericalCol].describe(quantiles).T)


numSummary(df, "age")

for col in numCols:
    numSummary(df, col)


def numSummary(dataframe, numericalCol, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numericalCol].describe(quantiles).T)
    if plot:
        dataframe[numericalCol].hist()
        plt.xlabel(numericalCol)
        plt.title(numericalCol)
        plt.show(block=True)


numSummary(df, "age", plot=True)

for col in numCols:
    numSummary(df, col, plot=True)


# Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi

def grabColNames(dataFrame, catTh=10, carTh=30):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """
    catCols = [col for col in df.columns if str(df[col].dtype) in ['object', 'category', "bool"]]
    numButCat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    catButCar = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    catCols = catCols + numButCat
    catCols = [col for col in catCols if col not in catButCar]
    numCols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    numCols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    numCols = [col for col in numCols if col not in catCols]
    print(f"Observations: {dataFrame.shape[0]}")
    print(f"Variables: {dataFrame.shape[1]}")
    print(f'cat_cols: {len(catCols)}')
    print(f'num_cols: {len(numCols)}')
    print(f'cat_but_car: {len(catButCar)}')
    print(f'num_but_cat: {len(numButCat)}')

    return catCols, numCols, catButCar


catCols, numCols, catButCar = grabColNames(df)


def catSummary(dataFrame, colName):
    print(pd.DataFrame({colName: dataFrame[colName].value_counts(),
                        "Ratio": 100 * dataFrame[colName].value_counts() / len(dataFrame)}))
    print("##########################################")


catSummary(df, "sex")
for col in catCols:
    catSummary(df, col)


def numSummary(dataframe, numericalCol, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numericalCol].describe(quantiles).T)
    if plot:
        dataframe[numericalCol].hist()
        plt.xlabel(numericalCol)
        plt.title(numericalCol)
        plt.show(block=True)

for col in numCols:
    numSummary(df, col, plot=True)

# BONUS
df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

catCols, numCols, catButCar = grabColNames(df)
def catSummary(dataframe, colName, plot=False):
    print(pd.DataFrame({colName: dataframe[colName].value_counts(),
                        "Ratio": 100 * dataframe[colName].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[colName], data=dataframe)
        plt.show(block=True)


for col in catCols:
    catSummary(df, col, plot=True)

for col in numCols:
    numSummary(df, col, plot=True)