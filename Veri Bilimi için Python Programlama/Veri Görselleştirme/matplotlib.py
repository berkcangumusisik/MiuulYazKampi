# Matplotlib Kütüphanesi
'''
* Pythonda veri görselleştirmenin atasıdır.
* Düşük seviye veri görselleştirme aracıdır.
* Kategorik değişken varsa sütun grafiği kullanılır.
* Sayısal değişken ise kutu grafiği ya da histogram kullanılır.
'''
import pandas as pd
import seabornLibrary as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/advertising.csv")
df = sns.load_dataset("titanic")
print(df.head())

plt.hist(df["age"])  # plt.hist() ile histogram çizdirir.
print(plt.show())  # plt.show() ile grafiği gösterir.

plt.boxplot(df["fare"])  # plt.boxplot() ile kutu grafiği çizdirir.
plt.show()

# Matplotlib'in Özellikleri
x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)  # plt.plot() ile grafiği çizdirir.
print(plt.show())

plt.plot(x, y, "o")  # plot ile önce x ve y değerlerini çizdirip sonra o değerini çizdirir.
print(plt.show())

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)
print(plt.show())

plt.plot(x, y, "o")
print(plt.show())

# marker
y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')  # Grafikteki her kırılım noktasına belirlediğimiz şekli koyar.
print(plt.show())

plt.plot(y,marker="*")
print(plt.show())

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

# line
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r")  # linestyle ile grafiğin çizgi tipini belirler. color ile rengi belirler.
print(plt.show())


# Multiple Lines

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

# Labels

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# Başlık
plt.title("Bu ana başlık")

# X eksenini isimlendirme
plt.xlabel("X ekseni isimlendirmesi")

plt.ylabel("Y ekseni isimlendirmesi")

plt.grid() # arkaplanını gösterir.
plt.show()

#Subplots (Çoklu Grafik)

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()


# 3 grafiği bir satır 3 sütun olarak konumlamak.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()