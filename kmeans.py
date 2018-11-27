# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:23:45 2018

@author: Yasin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax) #normunu buluyor yani noktalar arası uzaklığı

def k_means(k):
    f1 = duzenliVeri['PetalLengthCm'].values # karşılaştırma yapacağımız ilk özelliği alıyoruz
    f2 = duzenliVeri['PetalWidthCm'].values #karşılaştırma yapacağımız ikinci özelliği alıyoruz bunlara mean değerlerinden karar veriyoruz ona da parçalayarak bakabiliriz ben daha önceden parçaladığım için tekrar bakmadım
    X = np.array(list(zip(f1, f2))) # tek bir liste halince birleştiriyoruz gezmesi kolay olsun diye
    R_x = np.random.uniform(1, np.max(X), size=k) # rastgele x ve y kordinatları belirliyoruz sınıf sayımıza göre
    R_y = np.random.uniform(0, np.max(X)-4, size=k)
    R = np.array(list(zip(R_x, R_y)), dtype=np.float32) # tekrar sınıflarımızı tek boyutlu diziye indirgiyoruz
    R_old = np.zeros(R.shape) #yeni merkez noktaları ile eski merkez noktaları arasını karşılaştırmak için oluşturduğumuz temp değişken
    clusters = np.zeros(len(X)) # yeni sınıfları kayıt edeceğimiz listemiz
    error = dist(R, R_old, None) # yeni merkezle eski merkez arasındaki mesafeye bakıyoruz
    while error != 0: # yeni merkezle eski merkez eşitlenene kadar sınıf belirleme işlemine devam ediyoruz
        for i in range(len(X)): # girdi sayımız kadar dönmemiz lazım ki hepsini karşılaştırabilelim burda 150 girdi var
            distances = dist(X[i], R) #merkez ile her bir girdinin uzaklığını hesaplıyoruz
            cluster = np.argmin(distances) # en yakın noktayı sınıf olarak belirletiyoruz ve aşağıda sınıfını atıyoruz
            clusters[i] = cluster        
        R_old = deepcopy(R) #tüm elemanlar dolaşlınca artık bu merkezle işimiz bitiyor yenisine geçmeden önce eski merkezimizi şuanki ile güncelliyoruz
        for i in range(k): # burda da her bir sınıfımızın ortalama değerlerini yeni merkezimiz seçiyor ve yeniden işleme başlıyoruz
            points = [X[j] for j in range(len(X)) if clusters[j] == i]
            R[i] = np.mean(points, axis=0)
        error = dist(R, R_old, None) #eğer yukarıda değiştirdiğimiz yeni merkez ile esdki merkez arasında mesafe yoksa artık işimiz bitmiş demektir
    return X,clusters,R

iris_veri = pd.read_csv("iris.csv") #dosyayı dışardan okuyoruz
duzenliVeri = iris_veri.drop(["Id"],axis=1)  #dosyada ıd sütunu vardı onu kaldırdım işimize yaramadığı için
duzenliVeri["Sinif"] = [np.where(duzenliVeri.Species.unique() == each)[0][0] for each in duzenliVeri.Species] # her bir elemanın hangi sınıfa ait olduğunu buluyor ve yeni bir sütuna bunları yazıyorum

colorMap = np.array(["red","green","blue"]) #sınıflarımızın herbirini farklı renkte ifade edebilmek için renk scalası oluşturdum, yapmasaydık aşağıda 3 ayrı subplot yazmak zorundakalacaktık
plt.subplot(1,2,1) #1,2. konumun 1. elemanını yazıyorum demek, yani 1,2 lik bir grafik olacak ve ben ilkini şimdi çizdiriyorum demek
plt.scatter(duzenliVeri.PetalLengthCm,duzenliVeri.PetalWidthCm, color=colorMap[duzenliVeri.Sinif]) # gerçek sınıflara göre çizdiriyorum grafiği
X,clusters,R=k_means(3) #kmeans i hesaplatıyorum
plt.title("Gerçek Sınıflandırması") # ilk grafiğe isim veriyorum
plt.subplot(1,2,2) # artık 1.2 nin 2. grafiğini çizdircem demek 
dataFrames = pd.DataFrame(X) # daha rahat işlem yapmak için onu veritabanına benzetiyorum
clusters=clusters.astype(int) # gelen claster verisi float ama benim colormapim int o yüzden cast işlemi yapıyorum 
dataFrames["clusters"]=clusters # ve bu clasterları oluşturduğum yeni dataframe e ekliyorum
dataFrames.columns=["X","Y","cluster"] # sütunlara isim veriyorum
plt.scatter(dataFrames.X,dataFrames.Y, color=colorMap[dataFrames.cluster]) #yeni grafiği çizdiriyorum
plt.scatter(R[:, 0], R[:, 1], marker='*', s=200, c='black') # kmeans noktalarını ekrana bastırıyorum
plt.title('K Mean Sınıflandırması') # 2. grafiğe isim veriyorum
plt.show() # tüm grafikleri gösteriyorum









































