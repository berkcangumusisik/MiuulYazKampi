"""
Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız.
"""
l = [2, 13, 18, 93, 22]
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

print(even)
print(odd)