# Liste (List)

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.
# - [] içerisine yazılır ve , ile ayrılır.
# - Her tür veri tipi içeride olabilir.

notes = [1,2,3,4]
print(type(notes))
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
print(not_nam[0])
print(not_nam[5])
print(not_nam[6])
print(not_nam[6][1])

notes[0] = 99
print(notes)
print(not_nam[0:3])

#Liste Metodları (List Methods)
#len() => kaç elemandan oluştuğu bilgisini verir.
print(len(notes))
print(len(not_nam))

# append: Listenin sonuna eleman ekler.
notes.append(100)
print(notes)

# pop: indexe göre silme işlemi yapar.
notes.pop(1)
print(notes)

# insert: indexe göre eleman ekler
notes.insert(2,5)
print(notes)