# Karakter Dizileri(String)
print("John")
print("John")

name = "Berkcan"

# Çok Satırlı Karakter Dizileri => 3 tane tek tırnak ya da 3 çift tırnak içerisinde yazılır.

print(
    """
    Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool
    """
)

longStr = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""
print(longStr)

# Karakter Dizilerinin Elemanlarına Erişmek
# Python programlama dilinde index 0'dan başlar.
# İstenilen indexe erişimek için [] içerisinde yazılır.
print(name[0])
print(name[3])

# Karakter Dizilerinde Slice İşlemi => belirlenen indexten istenen indexe kadar almayı sağlar.
print(name[0:2])
print(longStr[0:10])

# String içerisinde karakter sorgulama
# in operatörü ile yapılır.
# Büyük küçük harf duyarlıdır.
print("Veri" in longStr)
print("veri" in longStr)
print("bool" in longStr)

#String Metotları

dir(str)

# len metodu => string değerin kaç elemandan oluştuğun verir.
print(len(name))
print(len("vahitkeskin"))
print(len("miuul"))

# upper() & lower(): küçük-büyük dönüşümleri
print(name.upper())
print(name.lower())

# replace: karakter değiştirir
hi = "Hello AI Era"
hi.replace("l", "p")
print(hi)

# split: Belli bir boşluğa ya da karaktere göre böler
print(hi.split())

# strip: Baştan ve sondan boşlukları kırpar.
print(" ofofo ".strip())
print("ofofo".strip("o"))

# capitalize : İlk harfi büyütür.
print("foo".capitalize())