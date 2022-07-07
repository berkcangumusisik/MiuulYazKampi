"""
Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız.
"""
l = [2, 13, 18, 93, 22]
even_list = []
odd_list = []

def func(l):
    even_local = []
    odd_local = []
    for num in l:
        if num % 2 == 0:
            even_local.append(num)
        else:
            odd_local.append(num)
    return even_local, odd_local


even_list, odd_list = func(l)
print(even_list)
print(odd_list)