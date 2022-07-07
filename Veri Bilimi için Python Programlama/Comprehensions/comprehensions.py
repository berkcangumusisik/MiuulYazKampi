# List Comprehension
salaries = [1000, 2000, 3000, 4000, 5000]

def newSalary(x):
    return x * 20 / 100 + x

nullList = []
for salary in salaries:
    nullList.append(newSalary(salary))
print(nullList)

nullList = []
for salary in salaries:
    if salary > 3000:
        nullList.append(newSalary(salary))
    else:
        nullList.append(newSalary(salary) * 2)
print(nullList)

print([newSalary(salary * 2) if salary < 3000 else newSalary(salary) for salary in salaries])
print(salary * 2 for salary in salaries)
print([salary * 2 for salary in salaries if salary < 3000])
print([salary * 2 if salary < 3000 else salary * 0 for salary in salaries])

print([newSalary(salary * 2) if salary < 3000 else newSalary(salary * 0.2) for salary in salaries])
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]


print(student.lower() if student in students_no else student.upper() for student in students)
print([student.upper() if student not in students_no else student.lower() for student in students])

# Dict Comprehension

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}



print({k: v ** 2 for (k, v) in dictionary.items()})
print({k.upper(): v for (k, v) in dictionary.items()})
print({k.upper(): v*2 for (k, v) in dictionary.items()})
