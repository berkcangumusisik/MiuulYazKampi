# lambda => Fonksiyonu tek satırda yazmayı sağlar.
# lambda parametre(ler) : yapılacak işlemler

summer = lambda a,b : a + b
print(summer(2,3))

# map => elinizdeki bir fonksiyona, elinizdeki bir datanın elemanlarını sırasıyla gönderir ve sonucu tek bir obje olarak geri döner.
salaries = [1000, 2000, 3000, 4000, 5000]

def newSalary(x):
    return x * 20 / 100 + x

newSalary(5000)

for salary in salaries:
    print(newSalary(salary))

print(list(map(newSalary, salaries)))

# del newSum
print(list(map(lambda x: x * 20 / 100 + x, salaries)))
print(list(map(lambda x: x ** 2 , salaries)))

# FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, list_store)))

# REDUCE
"""
Reduce fonksiyonu, döngüye sokabileceğiniz herhangi bir veri tipi içinde, veri tipinin içindeki tüm elemanları azaltarak dolaşan ve karşılaştırma yapmaya imkan tanıyan bir yapıdır.
"""
from functools import reduce
list_store = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, list_store))
