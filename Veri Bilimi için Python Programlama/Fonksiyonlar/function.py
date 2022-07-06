print("a", "b", sep="--")  # sep ile veriler arasına koymak istediğimiz içeriklerdir.
# Fonksiyonlar

# def fonksiyonAdi(varsa argümanlar):
#   kodlar


def calculate(x):
    print(x * 2)


calculate(5)

#iki argümanlı ya da iki parametreli bir fonnksiyon tanımlarken argümanlarlar ya da parametreler arasına , konur

def summer(arg1,arg2):
    print(arg1 + arg2)
summer(7, 8)

summer(8, 7)

summer(arg2= 8, arg1=7)


#Docstring => Ortak bir dilde bilgi notu eklemektir.
# Yaygın olarak numpy kullanılır.
# 3 bölümden oluşur.
# - 1. bölümde fonksiyonun ne yaptığı ifade edilir.
# - 2. bölümde parametrelerin tipleri ve görevi  ifade edilir.
# - 3. bölümde return bilgisi girilir.
def summer(arg1 ,arg2):
    """
    Sum of two numbers
    Parameters
    ----------
    arg1: float, int
    arg2: float, int

    Returns:
        int, float
    -------

    """
    print(arg1 ,arg2)


# Fonksiyonların gövdesi(Statement bölümleri)

def sayHi(string):
    print(string)
    print("Hi")
    print("Hello")

sayHi("Miuul")

def multiplication(a, b):
    c = a * b
    print(c)
multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon.

listStore = []

def addElement(a, b):
    c = a * b
    listStore.append(c)
    print(listStore)
addElement(1,8)
addElement(18,8)
addElement(180,10)


# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
# Fonksiyonun hiçbir değer verilmezse sabit bir değer verilmesidir.

def divide(a, b):
    print(a / b)


divide(1, 2)


def divide(a, b=2):
    print(a / b)


divide(10)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi("mrb")

# Fonksiyonları birbirini tekrar eden durumlarda kullanırız. DRY prensibini sağlar.

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)

# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak


def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


print(calculate(98, 12, 78) * 10)

a = calculate(98, 12, 78)
print(a)

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


print(type(calculate(98, 12, 78)))

# Fonksiyon İçerisinden Fonksiyon Çağırmak


def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


print(calculate(90, 12, 12) * 10)


def standardization(a, p):
    return a * 10 / 100 * p * p


print(standardization(45, 1))

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)


def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 19, 12)


# Lokal & Global Değişkenler (Local & Global Variables)
list_store = [1, 2]

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 9)