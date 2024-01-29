sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1: sayilar listesini while ile ekrana yazdirin. 

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# 2: Baslangiç ve bitis degerlerini kullanicidan alip aradaki tüm
#       tek sayilari ekrana yazdirin.

baslangic = int(input("baslangic: "))
bitis = int(input("bitis: "))

a = baslangic

while a < bitis:
    a += 1
    if i % 2 == 1:
        print(a)

# 3: 1-100 arasindaki sayilari azalan sekilde yazdirin.

b = 100

while b > 0:
    print(i)
    i -= 1

# 4: Kullanicidan alacaginiz 5 sayiyi ekranda sirali bir sekilde yazdirin.

numbers = []

c = 0

while c < 5:
    sayi = int(input("sayi"))
    numbers.append(sayi)
    c += 1

numbers.sort()
print(numbers)


# 5: Kullanicidan alacaginiz sinirsiz ürün bilgisini urunler listesi içinde sak
#       ** ürün sayisini kullaniciya sorun.
#       ** dictionary listesi yapisi (name, price) seklinde olsun.
#       ** ürün ekleme islemi bittiginde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input("kaç adet urun eklemek istiyorsunuz: "))
e = 0

while (e < adet):
    name = input("urun ismi: ")
    price = input("price fiyati: ")
    urunler.append({
        "name": name,
        "price": price
    })
    e += 1

for urun in urunler:
    print(f"""
    urun adi: {urun["name"]}
    urun fiyati: {urun["price"]}
""")
