# print() ekrana yazı yazmayı sağlar.
print("Hello World")

# Karakter Dizileri(Strings) ve Sayılar(Numbers)
print(9)
print("Hello AI Era")

'''
String ile number arasındaki farka bakıldığında stringler "" içerisinde yazılırken sayısal ifadeler boş yazılmaktadır.
'''

# type() fonksiyonu nesnenin(şey denmez nesne denir) veri tipini bulmayı sağlar (int, string, float, bool)
print(type(9))
print(type(9.2))
print(type("Berkcan"))

#Atamalar ve Değişkenler (Assignments & Variables)
'''
Değişkenler sayesinde oluşturduğumuz veriyi programın ilerleyen kısımlarında da kullanmayı sağlıyor.
Atama yaparken = ifadesi kullanılır.
'''

a = 9
print(a)
b = "Hello AI Era"
print(b)
c = 10
print(a * c)
print(a * 10)
d = a - c
print(d)

# Virtual Enviroment(Sanal Ortam)
'''
* İzole çalışma ortamları oluşturmak için kullanılan araçlardır.
* Farklı çalışmalar için oluşabilecek kütüphane ve versiyonlar için çalışmaları etkilemeyecek şekilde oluşturma imkanı sunar.
* conda, pipenv,venv,virtualenv örnek olarak verilebilir
'''

# Package Management(Paket Yönetimi) Araçları
'''
* pip
* pipenv
* conda
'''

# Sanal Ortamlar ve Paket Yönetimi Arasındaki İlişki
'''
* venv ve virtualenv paket yönetim aracı olarak pip kullanıyor.
* conda ve pipenv hem paket hem de sanal ortam yönetiminde kullanılıyor.
* pip paket yönetimi için kullanılır.
'''