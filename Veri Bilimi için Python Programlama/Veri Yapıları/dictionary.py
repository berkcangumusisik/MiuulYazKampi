# Dictionary(Sözlük)

# Değiştirilebilir.
# Normal şartlarda sırasızdır. Ama 3.7 versiyonuyla birlikte sıralı özelliği kazanmıştır.
# Her veri tipini içerisinde barındırır.
# {} içerisine yazılır. {key:value}
# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}
print("REG")

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

print(dictionary["CART"])

# Key Sorgulama

print("YSA" in dictionary)

# Key'e Göre Value'ya Erişmek => [""] ya da get metoduyla erişiriz.


print(dictionary["REG"])
print(dictionary.get("REG"))

# Value Değiştirmek

dictionary["REG"] = ["YSA", 10]
print(dictionary)


# Tüm Key'lere Erişmek

print(dictionary.keys())

# Tüm Value'lara Erişmek

print(dictionary.values())


# Tüm Çiftleri Tuple Halinde Listeye Çevirme
print(dictionary.items())

# Key-Value Değerini Güncellemek

dictionary.update({"REG": 11})


# Yeni Key-Value Eklemek

dictionary.update({"RF": 10})

print(dictionary)