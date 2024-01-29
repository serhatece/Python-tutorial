sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayilar 3'ün katidir ?
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)

# 2- Sayilar listesinde sayilarin toplami kactir ?
toplam = 0
for s in sayilar:
    toplam += s
print(toplam)

# 3- Sayilar listesindeki tek sayilarin karesini aliniz.
for s1 in sayilar:
    if(s1 % 2 == 1):
        print(s1 ** 2)



sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- Sehirlerden hangileri en fazla 5 karakterlidir ?
for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)


urunler = [
    {'name': 'samsung S6','price':'3000'},
    {'name': 'samsung 57','price':'4000'},
    {'name': 'samsung 58','price':'5000'},
    {'name': 'samsung S9','price':'6000'},
    {'name': 'samsung S10','price':'7000'}
]

# 5- Urünlerin fiyatlari toplam nedir ?
top = 0
for urun in urunler:
    fiyat = int(urun["price"])
    top += fiyat

print(top)

# 6- Ürünlerden fiyati en fazla 5000 olan ürünleri gösteriniz ?
for u in urunler:
    if(int(urun["price"] <= 5000)):
        print[u["name"]]

