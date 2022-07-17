"""
List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
harfe çeviriniz ve başına NUM ekleyiniz
# Beklenen Çıktı

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar:
# Numerik olmayanların da isimleri büyümeli.
# Tek bir list comp yapısı ile yapılmalı.
"""
import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
print(df.columns)