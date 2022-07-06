# Set(Küme)
# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

# difference(): İki kümenin farkı


set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
print(set1.difference(set2))
print(set2.difference(set1))

# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

# intersection(): İki kümenin kesişimi
print(set1.intersection(set2))

# union(): İki kümenin birleşimi
print(set1.union(set2))

# isdisjoint(): İki kümenin kesişimi boş mu?
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])
print(set1.isdisjoint(set2))

# issubset(): Bir küme diğer kümenin alt kümesi mi?
print(set1.issubset(set2))
print(set2.issubset(set1))

# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
print(set1.issuperset(set2))
print(set2.issuperset(set1))
