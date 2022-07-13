print("--------- Görev 1 -------------")
"""
Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
"""
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("datasets/advertising.csv")
df = sns.load_dataset("titanic")
print(df.head())
print("--------- Görev 2 -------------")
"""
Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
"""
print(df["sex"].value_counts())

print("--------- Görev 3 -------------")
"""
Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
"""
print(df.nunique())

print("--------- Görev 4 -------------")
"""
Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
"""

print(df["pclass"].nunique())

print("--------- Görev 5 -------------")
""" 
Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz
"""
print(df[["pclass", "parch"]].value_counts())

print("--------- Görev 6 -------------")
"""
Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
"""

print("embarked değişkenin tipi:", df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
print("embarked değişkenin tipi:", df["embarked"].dtype)

print("--------- Görev 7 -------------")
"""
Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.
"""
print(df[df["embarked"] == "C"])

print("--------- Görev 8 -------------")
"""
Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
"""
print(df[df["embarked"] != "S"])

print("--------- Görev 9 -------------")
"""
Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
"""
print(df.query('(age < 30) & (sex == "female")'))

print("--------- Görev 10 -------------")
"""
Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz
"""
print(df.query('(fare > 500) | (age > 70)'))

print("--------- Görev 11 -------------")
"""
Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
"""
print(df.isnull().sum())

print("--------- Görev 12 -------------")
"""
Görev 12: who değişkenini data frame'den çıkarınız.
"""
print(df.drop("who", axis=1).head())

print("--------- Görev 13 -------------")
"""
Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
"""
df["deck"].fillna(df["deck"].mode().iloc[0], inplace=True)
print(df.head())

print("--------- Görev 14 -------------")
"""
Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
"""
df["age"].fillna(df["age"].median(), inplace=True)
print(df.head())

print("--------- Görev 15 -------------")
"""
Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
"""
print(df.groupby(["sex", "pclass"]).agg({"survived": ["mean", "sum", "count"]}))

print("--------- Görev 16 -------------")
"""
Görev 16 : 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
"""

age_flag = df["age"].apply(lambda x: 1 if x < 30 else 0)
df["age_flag"] = age_flag
print(df.head())

print("--------- Görev 17 -------------")
"""
Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
"""
df = sns.load_dataset("tips")
print(df.head())

print("--------- Görev 18 -------------")
"""
Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz.
"""
print(df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]}))

print("--------- Görev 19 -------------")
"""
Görev 19: Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.
"""
print(df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]}))

print("--------- Görev 20 -------------")
"""
Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulunuz.
"""
print(df[["total_bill", "tip", "day"]].loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day"). \
      agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]}))

print("--------- Görev 21 -------------")
"""
Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
"""
print(df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].mean())

print("--------- Görev 22 -------------")
"""
Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
"""
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
print(df.head())

print("--------- Görev 23 -------------")
"""
Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz. Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacktır. Parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)
"""

female = df.groupby("sex").total_bill.mean()[0]
male = df.groupby("sex").total_bill.mean()[1]


def total_bill_flag(gender, total_bill):
    if gender == "Female" and total_bill < female:
        return 0
    elif gender == "Female" and total_bill >= female:
        return 1
    elif gender == "Male" and total_bill < male:
        return 0
    elif gender == "Male" and total_bill >= male:
        return 1


df["total_bill_flag"] = df.apply(lambda x: total_bill_flag(x.sex, x.total_bill), axis=1)
print(df.head())

print("--------- Görev 24 -------------")
"""
Görev 24 : total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.
"""

print(df.groupby(["sex", "total_bill_flag"]).total_bill_flag.count())

print("--------- Görev 25 -------------")
"""
Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
"""
df.sort_values("total_bill_tip_sum", ascending=False)
df_new = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
print(df_new)