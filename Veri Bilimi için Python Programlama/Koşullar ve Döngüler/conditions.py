# KOŞULLAR (CONDITIONS)
"""
if koşul1:
    koşul1 sağlanırsa çalışacak kodlar
elif koşul2:
    koşul2 sağlanırsa çalışacak kodlar
else:
    Hiçbir koşul doğru değilse çalışacak kodlar
"""
if 1 == 1:
    print("Something")

if 1 == 2:
    print("Something")


def number_check(number):
    if number == 10:
        print("Number is 10")

number_check(12)
number_check(10)

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(6)