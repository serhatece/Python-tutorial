import numpy as np

# np.array ile dizi oluşturma
result = np.array([1,3,5,7,9])

# np.arange ile aralıkta sayılar oluşturma
result = np.arange(1,10)

# Belirli aralıkta belirli adımlarla sayılar oluşturma
result = np.arange(10,100,3)

# Sıfırlardan oluşan dizi oluşturma
result = np.zeros(10)

# Birlerden oluşan dizi oluşturma
result = np.ones(10)

# Belirli aralıkta belirli sayıda eşit aralıklı değerler oluşturma
result = np.linspace(0,100,5)

# Belirli aralıkta belirli sayıda eşit aralıklı değerler oluşturma
result = np.linspace(0,5,5)

# Belirli aralıktaki rastgele bir tamsayı oluşturma
result = np.random.randint(0,10)

# 0'dan belirli bir sayıya kadar rastgele bir tamsayı oluşturma
result = np.random.randint(20)

# Belirtilen aralıktaki belirtilen sayıda rastgele tamsayı içeren dizi oluşturma
result = np.random.randint(1,10,3)

# [0,1) aralığında rastgele sayılardan oluşan dizi oluşturma
result = np.random.rand(5)

# Standart normal dağılıma göre rastgele sayılardan oluşan dizi oluşturma
result = np.random.randn(5)

# Diziyi yeniden şekillendirme
np_array = np.arange(50)
np_multi = np_array.reshape(5,10)

# Sütunlar boyunca toplamı hesaplama
print(np_multi.sum(axis=1))

# Satırlar boyunca toplamı hesaplama
print(np_multi.sum(axis=0))

# Rastgele sayılar oluşturma ve işlemler
rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()  # Maksimum değeri bulma
result = rnd_numbers.min()  # Minimum değeri bulma
result = rnd_numbers.mean() # Ortalama değeri bulma
result = rnd_numbers.argmax() # Maksimum değerin dizideki indeksini bulma
result = rnd_numbers.argmin() # Minimum değerin dizideki indeksini bulma

print(result)