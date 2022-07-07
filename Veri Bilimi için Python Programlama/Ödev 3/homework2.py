"""Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
kelime kelime ayırınız."""

text = "The goal is to turn data into information, and information into insight."
upper = text.upper()
print(upper.split(" "))
