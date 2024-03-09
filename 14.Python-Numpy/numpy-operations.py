import numpy as np

# Rastgele sayılardan oluşan diziler oluşturma
numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

# Dizileri yazdırma
print(numbers1)
print(numbers2)

# Dizi elemanları üzerinde farklı matematiksel işlemler yapma
result = numbers1 + numbers2
result = numbers1 + 10
result = numbers1 - numbers2
result = numbers1 - 10
result = numbers1 * numbers2
result = numbers1 * 10
result = numbers1 / numbers2
result = numbers1 / 10

# Trigonometrik fonksiyonlar, karekök ve logaritmik fonksiyonlar uygulama
result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

# İki boyutlu diziler oluşturma
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

# Dikey ve yatay birleştirme işlemleri
result = np.vstack((mnumbers1,mnumbers2))
result = np.hstack((mnumbers1,mnumbers2))

# Belirli bir koşulu sağlayan dizinin elemanlarını seçme
result = numbers1 >= 50
result = numbers1 % 2 == 0

# Koşulu sağlayan elemanları seçme ve yazdırma
print(numbers1[result])

# Koşul sonucunu yazdırma
print(result)