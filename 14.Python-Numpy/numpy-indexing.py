import numpy as np

# Dizi oluşturma
numbers = np.array([0,5,10,15,20,25,50,75])

# Belirli bir indeksteki değeri alma
result = numbers[5]

# Tersten belirli bir indeksteki değeri alma
result = numbers[-1]

# Belirli aralıktaki değerleri alma
result = numbers[0:3]

# Başlangıçtan belirli bir indekse kadar değerleri alma
result = numbers[:3]

# Belirli bir indeksten sona kadar değerleri alma
result = numbers[3:]

# Dizinin tüm elemanlarını alma
result = numbers[::]

# Dizinin ters çevrilmiş halini alma
result = numbers[::-1]

# İkinci boyutlu dizi oluşturma
numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])

# Belirli bir satırı alma
result = numbers2[0]

# Belirli bir satırı alma
result = numbers2[2]

# Belirli bir elemanı alma
result = numbers2[0,2]

# Belirli bir elemanı alma
result = numbers2[2,1]

# Tüm satırlardan belirli bir sütunu alma
result = numbers2[:,2]

# Tüm satırlardan belirli bir sütunu alma
result = numbers2[:,0]

# Tüm satırlardan belirli bir aralıktaki sütunları alma
result = numbers2[:,0:2]

# Son satırı alma
result = numbers2[-1,:]

# Belirli bir aralıktaki satır ve sütunları alma
result = numbers2[:2,:2]

# Referans ile kopya alma
arr1 = np.arange(0,10)
arr2 = arr1.copy()

# Değer değişimi
arr2[0] = 20

print(arr1)  # arr1 değişmemiş olmalı
print(arr2)  # arr2'nin ilk elemanı 20 olmalı