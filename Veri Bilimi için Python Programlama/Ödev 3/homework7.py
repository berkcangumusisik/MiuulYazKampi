"""
List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# Notlar:
# Tüm değişken isimleri büyük olmalı.
# Tek bir list comp ile yapılmalı.

# Beklenen çıktı:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']


"""
import seaborn as sns
df = sns.load_dataset("car_crashes")

b = [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]
print(b)