# DÖNGÜLER (LOOPS)

# for loop
"""
for donguDegiskeni  in dönülecekElemanlar:
    Gerekli kodlar
"""
students = ["John", "Mark", "Venessa", "Mariam"]
for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary* 20 / 100 + salary))

def newSalary(salary, rate):
    return int(salary * rate / 100 + salary)

print(newSalary(1500,10))
print(newSalary(2000,20))

for salary in salaries:
    print(newSalary(salary, 20))

salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(newSalary(salary, 15))

for salary in salaries:
    if salary > 3000:
        print(newSalary(salary, 10))
    else:
        print(newSalary(salary, 20))

# range => iki değer arasında sayı üretmeyi sağlar.
print(range(0,5))
for i in range(0,5):
    print(i)