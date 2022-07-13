#4. Hedef Değişken Analizi (Analysis of Target Variable)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/advertising.csv")
df = sns.load_dataset("titanic")
print(df.head())

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
def catSummary(dataframe, colName, plot=False):
    print(pd.DataFrame({colName: dataframe[colName].value_counts(),
                        "Ratio": 100 * dataframe[colName].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[colName], data=dataframe)
        plt.show(block=True)

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

df["survived"].value_counts()
catSummary(df, "survived")

# Hedef Değişkenin Kategorik Değişkenler ile Analizi

def targetSummaryWithCat(dataframe, target, categoricalCol):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categoricalCol)[target].mean()}), end="\n\n\n")

targetSummaryWithCat(df, "survived", "pclass")

for col in catCols:
    targetSummaryWithCat(df, "survived", col)
    print("##########################################")

# Hedef Değişkenin Sayısal Değişkenler ile Analizi
def targetSummaryWithCat(dataframe, target, numericalCol):
    print(dataframe.groupby(target).agg({numericalCol: "mean"}), end="\n\n\n")

targetSummaryWithCat(df, "survived", "age")

for col in numCols:
    targetSummaryWithCat(df, "survived", col)