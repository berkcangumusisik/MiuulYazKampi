"""
List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
"""
import seaborn as sns
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]
df.columns

newCols = [col for col in df.columns if col not in og_list]
newDf = df[newCols]
print(newDf)