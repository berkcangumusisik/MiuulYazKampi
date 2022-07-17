
###############################################
# Virtual Environment Oluşturma
###############################################

###############################################
# Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
###############################################

# conda create -n sbk python=3
# conda env list (tüm env görebilirsiniz)

###############################################
# Görev 2: Oluşturduğunuz environment'ı aktif ediniz.
###############################################

# conda activate sbk

###############################################
# Görev 3: Yüklü paketleri listeleyiniz.
###############################################

# conda list

###############################################
# Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.4.1 versiyonunu aynı anda indiriniz.
###############################################

# conda install numpy pandas=1.4.1

###############################################
# Görev 5: İndirilen Numpy'ın versiyonu nedir?
###############################################

# conda list

###############################################
# Görev 6: Pandas'ı upgrade ediniz. Yeni versiyon nedir?
###############################################

# conda upgrade pandas
# conda list

###############################################
# Görev 7: Numpy'ı environment'tan siliniz.
###############################################

# conda remove numpy


###############################################
# Görev 8: Seaborn kütüphanesini ve matplotlib kütüphanesini aynı anda güncel versiyonları ile indiriniz.
###############################################

# conda install seaborn matplotlib

###############################################
# Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
###############################################

#  conda env export > enviroment.yaml

###############################################
# Görev 10: Oluşturduğunuz environment'i siliniz.
###############################################
# İpucu: Önce environment'i deactivate ediniz.

# conda deactivate
# conda env remove -n sbk
