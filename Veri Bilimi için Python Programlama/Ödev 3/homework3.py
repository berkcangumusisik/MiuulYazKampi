"""
Verilen listeye aşağıdaki adımları uygulayınız
lst = ["D","A","T","A","S","C","I","E","N","C","E"]
"""
lst = ["D","A","T","A","S","C","I","E","N","C","E"]
#Adım 1: Verilen listenin eleman sayısına bakınız.
print(len(lst))
#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
print(lst[0])
print(lst[10])
#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
newList = lst[0:4]
print(newList)
#Adım 4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
print(lst)
#Adım 5: Yeni bir eleman ekleyiniz.
lst.append(1)
print(lst)
#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8,"N")
print(lst)