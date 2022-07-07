# Enumerate: Otomatik Counter/Indexer ile for loop


students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

A = []
B = []
for index,student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
print(A)
print(B)

#Uygulama - Mülakat sorusu
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]
def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
divide_students(students)

# alternating fonksiyonunun enumerate ile yazılması
def alternatingWithEnumarate(string):
    newString = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            newString += letter.upper()
        else:
            newString += letter.lower()
    print(newString)


alternatingWithEnumarate("hi my name is john and i am learning python")

