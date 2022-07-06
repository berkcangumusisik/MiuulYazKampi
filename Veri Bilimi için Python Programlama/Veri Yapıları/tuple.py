# Demet (Tuple)
# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.
# - () içerisine yazılır

t = ("john", "mark", 1, 2)
print(type(t))

print(t[0])
print(t[0:3])


t = list(t)
print(t)
t[0] = 99
t = tuple(t)
print(t)
