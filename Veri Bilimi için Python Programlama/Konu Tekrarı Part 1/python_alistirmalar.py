
###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4,"String",3.2, False]
type(l)
# Sıralıdır
l[5]

# Kapsayıcıdır
# birden fazla tip eleman bulunur.

# Değiştirilebilir
l[0] = 90

l



d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

# Değiştirilebilir
d["Name"] = "Saltuk"
d
# Kapsayıcı
# birden fazla tip eleman bulunur.

# Sırasız
d[0]

# Key değerleri farklı olacak



t = ("Machine Learning", "Data Science", 5)
type(t)
# Değiştirilemez
t[0] = "Python"
# Kapsayıcı
# birden fazla tip eleman bulunur.

# Sıralı
t[0]



s = {"Python", "Machine Learning", "Data Science", 3 , 3 }
type(s)
s
# Değiştirilebilir
s.add(8)
s
# Sırasız + Eşsiz
s[0]

# Kapsayıcı
# birden fazla tip eleman bulunur.



###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

text.upper().replace(",", " ").replace(".", " ").split()



###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.

lst.pop(8)

# Adım 5: Yeni bir eleman ekleyin.

lst.append(101)
lst
# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, "N")
lst
###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict.update({"Daisy":["England", 13]})
dict
# 2. yol

dict['Daisy'][1] = 13
dict

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict["Ahmet"] = ["Turkey", 24]
dict

# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")

dict

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def oddEven(myList):
    #output = [[], []]
    odd = []
    even = []
    for i in myList:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd

even, odd = oddEven(l)





###############################################
# GÖREV 6: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
###############################################

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

import seaborn as sns
df = sns.load_dataset("car_crashes")

df.head()
df.columns
df.info()
df["total"].dtype


["NUM_" + i.upper() if df[i].dtype != "O" else i.upper() for i in df.columns]


# [ ifYapılacak if condition else elseYapılacak  for]





###############################################
# GÖREV 7: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
###############################################

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

# [ ifYapılacak if else elseYapılacak  for]


import seaborn as sns
df = sns.load_dataset("car_crashes")


[col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


###############################################
# Görev 8: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
###############################################

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


og_list = ["abbrev", "no_previous"]


import seaborn as sns
df = sns.load_dataset("car_crashes")

df.head()
df.columns

new_cols = [col for col in df.columns if col not in og_list]
df[new_cols].head()