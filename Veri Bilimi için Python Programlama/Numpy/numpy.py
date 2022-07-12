"""
* Numpy bilimsel hesaplamalar, çok boyutlu arraylar ve matrisler üzerinde yüksek derecede çalışma imkanı sağlar.
* Numpy kütüphanesinin listelerden farkı verimli veri saklama ve vektörel işlemlerin yapılmasıdır.
* Numpy kütüphanesini öncelikli olarak import etmemiz gerekir.
* Daha az çabayla daha çok iş yapmayı sağlar
"""

import numpy as np  # Numpy kütüphanesini import ettikten sonra as ile kullanacağımız isimleri belirledik.

# Klasik Python
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
print(ab)

# Numpy
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
ab = a * b
print(ab)

# Numpy Array'leri oluşturmak
# Numpy arrayleri oluşturmak için np.array() fonksiyonunu kullanabiliriz.

print(np.array([1, 2, 3, 4, 5]))
print(type(np.array([1, 2, 3, 4, 5])))

print(np.zeros(10, dtype=int))  # np.zeros() fonksiyonu ile girilen 0 kadar 0 arrayi oluşturur.

print(np.random.randint(0, 10, 10))
# np.random.randint() fonksiyonu ile başlangıç değeri ile bitiş değeri arasında istenilen adet kadar rasgele sayı oluşturur.

np.random.normal(10, 4, (3, 4))
# np.random.normal() fonksiyonu ile istenilen değerlerden oluşan normal veri oluşturur.


# Numpy Array Özellikleri
# Numpy arraylerinin özelliklerini öğrenmek için np.info() fonksiyonunu kullanabiliriz.
# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

d = np.random.randint(10, size=5)
print(d.ndim)
print(d.shape)
print(d.size)
print(d.dtype)

# Yeniden Şekillendirme (Reshaping)

print(np.random.randint(1, 10, size=9))
print(np.random.randint(1, 10, size=9).reshape(3, 3))

ar = np.random.randint(1, 10, size=9)
print(ar.reshape(3, 3))
print(ar)
# reshape() fonksiyonu ile array'in boyutlarını değiştirebiliriz.

x = np.random.randint(10, size=10)
print(x[0])
print(x[0:5])
x[0] = 999
print(x)

m = np.random.randint(10, size=(3, 5))
print(m)
print(m[0, 0])
print(m[1, 1])
m[2, 3] = 999
print(m)

m[2, 3] = 2.9
print(m)

print(m[:0])
print(m[1:])
print(m[0:2, 0:3])

# Fancy Index
v = np.arange(0, 30, 3)  # arange() fonksiyounu 3 parametre alır. arange(start, stop, step)

print(v[1])
print(v[4])
catch = [1, 2, 3]
print(v[catch])

# Numpy Koşullu İşlemler
n = np.array([1, 2, 3, 4, 5])

# 3'ten küçük olanlarını al
# Klasik döngü ile
print("Klasik Döngü")
ab = []
for i in n:
    if i < 3:
        ab.append(i)
print(ab)

# Numpy ile
print("Numpy")
ab = n[n < 3]
print(ab)

print(n[n > 3])
print(n[n != 3])
print(n[n == 3])
print(n[n >= 3])

# Matematiksel İşlemler (Mathematical Operations)
n = np.array([1, 2, 3, 4, 5])

# Numpy array içerisinde matematiksel işlemler yaparken n bir numpy array ise n * 2 dediğimiz zaman tüm değerleri 2 ile çarpar.

print(n / 5)
print(n * 5 / 10)
print(n ** 2)
print(n - 1)

# Numpy da matematiksel işlemleri yaparken numpy özel fonksiyonlarını da  kullanabiliriz.
print(np.subtract(n, 1))  # subtract() fonksiyonu ile girilen değerleri ekiltir.
print(np.add(n, 1))  # add() fonksiyonu ile girilen değerleri ekler.
print(np.mean(n))  # mean() fonksiyonu ile girilen değerlerin ortalamasını alır.
print(np.min(n))  # min() fonksiyonu ile girilen değerlerin en küçüğünü alır.
print(np.max(n))  # max() fonksiyonu ile girilen değerlerin en büyüğünü alır.
print(np.sum(n))  # sum() fonksiyonu ile girilen değerlerin toplamını alır.
print(np.var(n))  # var() fonksiyonu ile girilen değerlerin varyansını alır.

## Numpy ile iki bilinmeyenli denklemler
#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])
print(np.linalg.solve(a, b)) # linalg.solve() fonksiyonu ile denklemi çözümler.