"""
Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
- conda create n berkcan
Görev 2: Oluşturduğunuz environment'ı aktif ediniz.
- conda activate berkcan
Görev 3: Yüklü paketleri listeleyiniz.
- conda list
Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
# conda install numpy pandas=1.2.1
Görev 5: İndirilen Numpy'ın versiyonu nedir?
# conda list
Görev 6: Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
-  1.4.3
Görev 7: Numpy'ı environment'tan siliniz.
- conda remove numpy
Görev 8: Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
- conda install seaborn matplotlib
Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
- conda env export > enviroment.yaml
Görev 10: Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.
- conda deactivate
- conda env remove -n berkcan
"""