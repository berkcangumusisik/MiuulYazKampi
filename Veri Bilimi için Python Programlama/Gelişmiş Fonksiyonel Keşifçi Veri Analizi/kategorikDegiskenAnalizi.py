# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/advertising.csv")
df = sns.load_dataset("titanic")
print(df.head())

print(df["embarked"].value_counts())
print(df["sex"].unique())  # unique() fonksiyonu ile birbirinden farklı kaç kategori olduğunu gösterir.
print(df["class"].nunique())  # kaç sınıf olduğunu verir.

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

print(df[catCols].nunique())

print([col for col in df.columns if col not in catCols])


def catSummary(dataFrame, colName):
    print(pd.DataFrame({colName: dataFrame[colName].value_counts(),
                        "Ratio": 100 * dataFrame[colName].value_counts() / len(dataFrame)}))
    print("##########################################")


catSummary(df, "sex")
for col in catCols:
    catSummary(df, "sex")


def catSummary(dataFrame, colName, plot=False):
    print(pd.DataFrame({colName: dataFrame[colName].value_counts(),
                        "Ratio": 100 * dataFrame[colName].value_counts() / len(dataFrame)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataFrame[colName], data=dataFrame)
        plt.show(block=True)


catSummary(df, "sex", plot=True)

for col in catCols:
    if df[col].dtypes == "bool":
        print("sdfsdfsdfsdfsdfsd")
    else:
        catSummary(df, col, plot=True)

df["adult_male"].astype(int)
print(df["adult_male"])

for col in catCols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        catSummary(df, col, plot=True)
    else:
        catSummary(df, col, plot=True)


def catSummary(dataFrame, colName, plot=False):
    if dataFrame[colName].dtypes == "bool":
        dataFrame[colName] = dataFrame[colName].astype(int)
        print(pd.DataFrame({colName: dataFrame[colName].value_counts(),
                            "Ratio": 100 * dataFrame[colName].value_counts() / len(dataFrame)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataFrame[colName], data=dataFrame)
            plt.show(block=True)
    else:
        print(pd.DataFrame({colName: dataFrame[colName].value_counts(),
                            "Ratio": 100 * dataFrame[colName].value_counts() / len(dataFrame)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataFrame[colName], data=dataFrame)
            plt.show(block=True)


catSummary(df, "sex", plot=False)
