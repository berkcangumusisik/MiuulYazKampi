"""
Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
İş Problemi
Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
seviye tabanlı (level based) yeni müşteri tanımları (persona)
oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
istemektedir.
Örneğin:
Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
kullanıcının ortalama ne kadar kazandırabileceği belirlenmek
isteniyor.

Veri Seti Hikayesi
Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
kullanıcı birden fazla alışveriş yapmış olabilir.

Değişkenler
PRICE – Müşterinin harcama tutarı
SOURCE – Müşterinin bağlandığı cihaz türü
SEX – Müşterinin cinsiyeti
COUNTRY – Müşterinin ülkesi
AGE – Müşterinin yaşı
"""

print("------------ GÖREV 1 ------------")
print("------------ Soru 1 ------------")
# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("persona.csv")
print(df.head())

print("------------ Soru 2 ------------")
"""
Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
"""
print(df["SOURCE"].nunique())

print("------------ Soru 3 ------------")

"""
Soru 3: Kaç unique PRICE vardır?
"""
print(df["PRICE"].nunique())

print("------------ Soru 4 ------------")
"""
Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
"""
print(df["PRICE"].value_counts())

print("------------ Soru 5 ------------")
"""
Soru 5: Hangi ülkeden kaçar tane satış olmuş?
"""
print(df.groupby("COUNTRY").PRICE.count())

print("------------ Soru 6 ------------")
"""
Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
"""

print(df.groupby("COUNTRY").PRICE.sum())

print("------------ Soru 7 ------------")
"""
Soru 7: SOURCE türlerine göre satış sayıları nedir?
"""

print(df["SOURCE"].value_counts())

print("------------ Soru 8 ------------")
"""
Soru 8: Ülkelere göre PRICE ortalamaları nedir?
"""
print(df.groupby("COUNTRY").agg({"PRICE": "mean"}))

print("------------ Soru 9 ------------")
"""
Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
"""
print(df.groupby("SOURCE").agg({"PRICE": "mean"}))

print("------------ Soru 10 ------------")
"""
Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
"""
print(df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"}))

print("------------ Görev 2 ------------")
"""
COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazanç nedir?
"""
print(df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}))

print("------------ Görev 3 ------------")

"""
Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a göre uygulayınız.
Çıktıyı agg_df olarak kaydediniz.
"""

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
print(agg_df)

print("------------ Görev 4 ------------")
"""
Görev 4: Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.
"""

agg_df = agg_df.reset_index()
print(agg_df)

print("------------ Görev 5 ------------")
"""
Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
 • Aralıkları ikna edici şekilde oluşturunuz.
 • Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'
"""
myLabels = ["0_18", "19_23", "24_30", "31_40", "41_70"]
agg_df["AGE_CAT"] = pd.cut(agg_df.AGE, bins=[0, 18, 23, 30, 40, 70], labels=myLabels)

print(agg_df.head())
print("------------ Görev 6 ------------")
"""
Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
• Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
• Yeni eklenecek değişkenin adı: customers_level_based
• Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.
"""
agg_df["customer_level_based"] = agg_df[["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]].apply("_".join, axis=1)
agg_df.customer_level_based.value_counts()
new_persona = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})
new_persona.reset_index(inplace=True)
new_persona.customer_level_based.value_counts()
new_persona["customer_level_based"] = new_persona.customer_level_based.apply(lambda x: x.upper())
print(new_persona.head())

print("------------ Görev 7 ------------")
"""
Yeni müşterileri (personaları) segmentlere ayırınız.
• Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
• Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
• Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
"""
new_persona["SEGMENT"] = pd.qcut(new_persona["PRICE"], 4, labels=["D", "C", "B", "A"])
print(new_persona.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]}))



print("------------ Görev 8 ------------")
"""
Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
• 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
• 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
"""
user1 = "TUR_ANDROID_FEMALE_31_40"
print(new_persona[new_persona.customer_level_based == user1])

user2 = "FRA_IOS_FEMALE_31_40"
print(new_persona[new_persona.customer_level_based == user2])



