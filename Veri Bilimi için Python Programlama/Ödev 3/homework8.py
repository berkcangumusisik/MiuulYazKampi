"""
List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

# og_list = ["abbrev", "no_previous"]

# Notlar:
# Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.

# Beklenen çıktı:

#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630
"""
import seaborn as sns
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]
df.columns

newCols = [col for col in df.columns if col not in og_list]
newDf = df[newCols]
print(newDf)