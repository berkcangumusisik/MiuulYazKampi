"""
List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazınız.
"""
import seaborn as sns
df = sns.load_dataset("car_crashes")

b = [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]
print(b)