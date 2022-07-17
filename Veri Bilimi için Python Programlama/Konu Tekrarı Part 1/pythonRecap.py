



# RECAP

# Ders Özeti:
# 1- Sanal Ortam (Virtual Environment)
# 2- Python
#   2.1- Veri Yapıları (Data Structures)
#   2.2- Fonksiyonlar (Functions)
#   2.3- Koşullar (Conditions)
#   2.4- Döngüler (Loops)
#   2.5- Comprehensions

# Mülakat Soruları & Alıştırmalar

# Neden Pycharm? Notebook'da iyiydik...
# Jupyter sunum için iyi. (Data Analyst)
# Product kısmına geçmek için Jupyter kullanılamaz.
# Daha kompleks özellikler kullanabilmek için Pycharm
# Terminal, Console yapısı
# Kütüphanelerin içini görüntüleme, env yönetimi vs vs.


# 1- Sanal Ortam (Virtual Environment)

# Virtual Environment Nedir?
"""
İzole çalıştırma ortamları oluşturmak için kullanılan araçlardır.
Farklı çalışmalar için oluşturulabilecek farklı kütüphane ve versiyon ihtiyaçlarını çalışmalar birbirini etkilemeyecek şekilde oluşturma imkanı sağlar.
"""


# Sadece paket yönetimiyle ilgilendiğimde hangisini kullanırım? Pip/Conda?
"""
Pip
"""

# Hem paket yönetimi hem sanal ortam yönetimi ihtiyacımız varsa hangisini kullanırız?
"""
Conda
"""


# ---------------------------------------------------------------

# 2- Python
#   2.1- Veri Yapıları (Data Structures)


# SAYILAR

# int
a = 5
type(a)

#float
b = 5.5
type(b)

#complex
c = 2j +4
type(c)

# işlem  yapalım
int(a + b)

print(a + b)


# Boolean

True
type(False)

1 == 1
1 == 2

2 > 3
2 < 3

2 >= 2
2 <= 2

###############################################
# Liste (List)
###############################################

x = ["a", "b", "c"]
x
type(x)

x[0]
# - Değiştirilebilir
x[0] = "x"
x

# - Sıralıdır. Index işlemleri yapılabilir.
x[0]
x[1]

# - Kapsayıcıdır.
liste = ["a", 2, 3.5, True]



###############################################
# Liste Metodları (List Methods)
###############################################

dir(liste)

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(liste)

#######################
# append: eleman ekler
#######################

liste.append(100)
liste
#######################
# pop: indexe göre siler
#######################

liste.pop(0)
liste
liste.pop()
liste
#######################
# insert: indexe ekler
#######################
liste
liste.insert(2, 99)
liste


###############################################
# Sözlük (Dictionary)
###############################################

x = {"name": "Ahmet", "Age": 22}
x
type(x)

# Değiştirilebilir.
x["name"] = "Saltuk"
x

# Sırasız. (3.7'den sonra sıralı. OrderedDict)
x[0]

# Kapsayıcı.
x = {"name": "Ahmet", "Age": 22}
# "Ahmet" = String / 22 = int


#######################
# Key Sorgulama
#######################

"name" in x
"Ahmet" in x

#######################
# Key'e Göre Value'ya Erişmek
#######################

dictionary = {"Ahmet": ["İstanbul", 20],
              "Ayşe": ["Ankara", 25],
              "Mehmet": ["İzmir", 30]}

dictionary["Ahmet"]

dictionary["Ahmet"][0]

dictionary.get("Ayşe")

#######################
# Value Değiştirmek
#######################
dictionary["Ahmet"] = ["Antalya", 22]
dictionary
#######################
# Tüm Key'lere Erişmek
#######################
dictionary.keys()

#######################
# Tüm Value'lara Erişmek
#######################

dictionary.values()


#######################
# Key-Value Değerini Güncellemek
#######################

dictionary
dictionary.update({"Mehmet": ["Tekirdağ",40]})
dictionary

dictionary.update({"Akın":["Bursa",30]})
dictionary

#######################
# Yeni Key-Value Eklemek
#######################

dictionary.update({"Samet": ["İstanbul",35]})

dictionary

###############################################
# Demet (Tuple)
###############################################

x = ("a", "b", "c")
x
type(x)


# - Değiştirilemez.
x[0] = "x"

# - Sıralıdır.
x[0]

# - Kapsayıcıdır.
x = ("a", 5, 2.5)


# Mülakat Sorusu
# Tuple ile Listenin Farkı nedir?
"""
Tuple'ın değiştirilemez, Liste'nin değiştirilebilir olması.
"""


# Mülakat Sorusu
# Tuple'ı hangi durumlarda listenin yerine tercih ederiz?
"""
Değiştirilmemesi gereken veriler tutuyorsanız tuple tercih etmelisiniz.
"""


# Bilgi:
# Tuplelar Listelerden daha verimlidir. Herhangi bir elemanı değiştirememe haricinde eleman ekleyip çıkaramazsınız da dolayısıyla ramde ekstra yer tutmuyor hiçbir zaman.


###############################################
# Set
###############################################

x = {"x", "y", "z"}
x
type(x)


# - Değiştirilebilir.
x.add(2)
x.update([3,4,5])
x

x.discard(2)
x.remove(3)
x
# Farkları ne?

x.discard(8)
x.remove(8) # error

# - Sırasız + Eşsizdir.
x[0]
x
x.update([4,4,4,4,4])
x
# - Kapsayıcıdır.
x = {1, "a", 2.5}



#######################
# difference(): İki kümenin farkı
#######################

set1 = {1, 3, 5}
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1

#######################
# intersection(): İki kümenin kesişimi
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


#######################
# union(): İki kümenin birleşimi
#######################

set1.union(set2)
set2.union(set1)


###############################################
# Karakter Dizileri (Strings)
###############################################

name = "Saltuk"
name = 'Saltuk'

print("Hello 'Saltuk'")
print('Hello "Saltuk"')

#######################
# Çok Satırlı Karakter Dizileri
#######################

long_str = """Seyahat etmeyenler.
Yavaş yavaş ölürler
Okumayanlar, müzik dinlemeyenler,
Vicdanlarında hoşgörüyü barındıramayanlar.
"""


print(long_str)

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name
name[0]
name[1]

name[-1]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2]

long_str[0:10]

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str

"Seyahat" in long_str
"seyahat" in long_str
"öl" in long_str



###############################################
# String (Karakter Dizisi) Metodları
###############################################

dir(str)

#######################
# len
#######################

name = "Vahit"
type(name)


len(name)

len("miuul")

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################
"VAHIT".lower()


name.upper()
"hello".upper()
"HELLO".lower()


#######################
# replace: karakter değiştirir
#######################

isim = "Ersun Yanal"
isim = isim.replace("u", "a")

#######################
# split: böler
#######################

isim.split()

#######################
# strip: kırpar
#######################
isim = "**miuul**"
isim
isim.strip("*")

isim.rstrip("*")

#######################
# capitalize: ilk harfi büyütür
#######################

"pablo".capitalize()


"pablo".startswith("w")

"Pablo".startswith("p")


###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################
# Fonksiyon ne işe yarar?
# - Don't Repeat Yourself (DRY)


def selam():
    selam = "selamlar"
    print(selam)
    return selam

kelime = selam()
kelime

def seslen(kelime):
    return kelime

seslen("hey")

kelime = seslen("hey")
kelime


kelime = seslen("merhaba")

kelime

def seslen(kelime):
    print("kelimeyi kaydediyorum...")
    return kelime

kelime = seslen("Hey")
kelime


kelime*5

seslen("Hey") * 5
seslen("Hey").upper()


# Şimdiki yıl ve doğum yılı bilgilerini argüman olarak alan ve yaşı hesaplayan fonksiyonu yazınız.


def age(curr_year, birth_year):
    agee = curr_year - birth_year
    return agee

yas = age(2022, 2000)

yas * 5




def age(current_year, birth_year):
    print(current_year - birth_year)

age(2022, 2000)

age(1996, 2022)


# ön tanımlı argüman/parametre


def age(current_year=2022, birth_year= 2000):
    print(current_year - birth_year)

age()
age(2000, 1980)



# Fonksiyon İçerisinden Fonksiyon Çağırmak
def age(current_year=2022, birth_year= 1996):
    return current_year - birth_year


def sigorta(current_year, birth_year, Work_year):
    yas = age(current_year, birth_year)
    year = current_year - Work_year
    return yas * year

sigorta(2022, 2000, 2018)

"""
def age(current_year=2022, birth_year= 1996):
    print(current_year - birth_year)
    
Bu fonksiyon ile çağırsaydık çalışmazdı.
"""


# Docstring

def sum(arg1, arg2):
    """
    Sum of two numbers

    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """
    return arg1 + arg2

sayi = sum(3,5)
sayi


###############################################
# KOŞULLAR (CONDITIONS)
###############################################

def passed(mark):
    if mark == 60:
        print("sınırda geçtiniz")
        return "sınırda"+str(mark)
    elif mark > 60:
        print("geçtiniz")
        return "geçtin "+str(mark)
    else:
        print("kaldınız")
        return "kaldın"+str(mark)

passed(70)


exam_notes = [10,20,30,40,50,60,70]


for i in exam_notes:
    passed(i)

[passed(i) for i in exam_notes]


#######################
# break & continue & while
#######################
names = ["a", "b", "c", "d", "e"]


for name in names:
    if name == "c":
        break
    print(name)



for name in names:
    if name == "c":
        continue
    print(name)



# while


number = 1

while number < 20:
    print(number)
    #number += 1



# Enumerate: Otomatik Counter/Indexer ile for loop


names = ["ahmet", "mehmet", "saltuk", "cemal"]

for i, name in enumerate(names):
    print(i+1, name)




###############################################
# lambda
###############################################

def sum(a, b):
    return a + b

sum(1, 3)


new_sum = lambda a, b: a * b

new_sum(4, 5)


# map, filter, reduce


###############################################
# COMPREHENSIONS
###############################################

#######################
# List Comprehension
#######################

# If-Else:

# [ [ifSonuç] if [koşul]  else [elseSonuç] for i in [...] ]


# If:
# [ [ifSonuç] for i in [...]  if [koşul] ]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

liste = []
for x in fruits:
    if "a" in x:
        liste.append(x)

liste


newlist = [x for x in fruits if "a" in x]

newlist

newlist = [x for x in fruits if "a" not in x]

newlist


liste = []
for x in fruits:
    if "a" in x:
        liste.append(x)
    else:
        liste.append("no a")


liste

newlist = [x if "a" in x else "no a" for x in fruits]

newlist


# 100'e kadar sayılarda 2 ve 5 e tam kalanlı bölünen sayıları listeye ekle

liste = []
for y in range(100):
    if (y%2 == 0) & (y%5 == 0):
        liste.append(y)

liste

"""
& = ve
| = veya
^ = ya da
"""
num_list = [y for y in range(100) if (y % 2 == 0) | (y % 5 == 0)]
print(num_list)




###########################################
# MÜLAKAT-ALIŞTIRMA SORULARI
###########################################

# Sicaklik birimlerinden Celsius'u Kelvine ceviren fonksiyonu yaziniz. (kelvin = celcius + 273)


def hesapla(celcius):
    kelvin = celcius + 273
    print(kelvin)

    return kelvin

kelvin = hesapla(30)

kelvin

# Yaş bilgisi argümanlı bir fonksiyon yazın 18 yaş altı için giremezsin üstü için hoş geldin yazsın



def yasSiniri(yas):
    if yas < 18:# False
        print("giremezsin")
        return "giremezsin"
    elif yas < 21: # True
        print("velinle girebilirsin")
    else:
        print("hoş geldin")
        return "hoş geldin"

yasSiniri(17)


# Asagidaki degiskenleri kullanarak dersin matematik olup olmadigini kontrol eden, matematik ise "Matematik sinavi aciklandi" ifadesi yazdiran,
# ders matematikse ayrica puanin 65'ten buyuk olup olmadigini kontrol eden ve
# 65'ten buyuk ise 'Sinavi Gectiniz' ifadesini cikti olarak yazan kodlari yaziniz.

ders = "Matematik"
puan = 70


def dersKontrol(ders, puan):
    if ders.lower() == "matematik":
        print("Mat sınavı açıklandı")
        if puan > 65:
            print("geçtin")
        else:
            print("kaldın")
    else:
        print("Mat sınavı açıklanmadı")

dersKontrol(ders, puan)






# Asagida verilen A listesindeki elemanlari for dongusu kullanarak B listesine tasiyiniz.

A = [10, 11, 12, 13, 14, 15, 16]
B = []

def move(liste1, liste2):
    for i in liste1:
        liste2.append(i)

    liste1 = []
    return liste1, liste2

list1, list2 =move(A, B)

list1
list2




# 0'dan 50ye kadar olan sayıları even ve odd listelerine ekleyiniz.


even = []
odd = []

for i in range(50):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even
odd



# Argüman olarak girilen sayının karesini alan fonksiyonu yazınız.


def square(n):
    squar = n**2

    return squar

square(5)

# Argüman olarak girilen 2 sayının üssünü alan fonksiyonu yazınız. power(2,3) -> 2^3 = 8


def power(a, b):
    powerr = a ** b
    # print(powerr)

    return powerr

pow = power(2,3)
pow



# Bir sayı listesi alıp bu listenin içindeki tüm elemanları toplayan fonksiyon

sampleList = [33,22,45,66,53,124]


def sumUp(x):
    sum_ = 0
    for i in x: # 33, 22, 45
        sum_ += i
        # 0 + 33 == 33
        # 33 + 22 == 55
        # 55 + 45 == 100
        print(sum_)

    return sum_

sumUp(sampleList)

# unique elemanları döndüren fonksiyonu yazınız.

nonUniquee = [1,1,1,2,3,4,4,4,5,5,6,6,7,8]


def nonUnique(a):
    myList = list(set(a))

    return myList

nonUnique(nonUniquee)


# Aşağıdaki şekilde string değiştiren bir fonksiyon yazmak istiyoruz.

# Before = "hi my name is john and i am learning python"
# After = "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"


def alternating(string):
    new_string = ""

    for index in range(len(string)):
        if index % 2 == 0:
            new_string += string[index].upper()
        else:
            new_string += string[index].lower()
    return new_string

alternating("hi my name is john and i am learning python")



# Yukarıdaki soruyu enumerate kullanarak çözünüz.


def alternating(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string

alternating("hi my name is john and i am learning python")


# For dongusu kullanarak arguman olarak girilen sayinin faktöriyelini hesaplayan fonksiyonu yaziniz. *****

for i in range(5):
    print(i+1)

def faktoriyel(value):
    a = 1
    for i in range(value,0, -1):
        a *= i
    return a

faktoriyel(5)




def faktoriyel(value):
    a = 1
    for i in range(value):
        a *= (i+1)
    return a

faktoriyel(3)



# Bonus: içeri istediğin kadar argüman girebildiğin bir fonksiyonda girdiğin tüm sayıları toplayan fonksiyonu yazınız.


def function(*args):
    num = 0

    for i in args:
        num = num + i

    return num

function(1,2,3,20,30,50)



# fruits listesinde kelime uzunluğu 5'den küçük olanları getir.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


liste = []
for i in fruits:
    if len(i) < 5:
        liste.append(i)

liste


fruitss = [i for i in fruits if len(i) < 5]
fruitss


# Hitters veri setinde int64 tipindeki değişkenleri getir.
import pandas as pd

df = pd.read_csv("datasets/hitters.csv")
df.info()

df.columns

liste = [col for col in df.columns if df[col].dtype == "int64"]
liste




# Hitters veri setinde object tipindeki değişkenleri getir.
import pandas as pd

df = pd.read_csv("datasets/hitters.csv")
df.info()

liste = [col for col in df.columns if df[col].dtype == "O"]


# tüm değişkenlerde gez object tipindekileri büyük harfle yaz.

liste = [col.upper() if df[col].dtype == "O" else col.lower() for col in df.columns]
liste


# [ ifSonuç if koşul  else elseSonuç for i in ... ]


# [ ifSonuç for i in ...  if koşul]

