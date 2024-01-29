"""
    1-10 arasinda rastgele üretilecek bir sayiyi asagi yukari ifadeleri ile
    buldurmaya calisin. (hak = 5)
    ** "random modulü" için "python random" seklinde arama yapin.
    ** 100 üzerinden puanlama yapin. Her soru 20 puan.
    ** Hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi
    üzerinden hesaplansin.
"""

import random

sayi = random.randint(1,10)
can = int(input("kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0
puan = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}.defada bildiniz. Toplam puan: {100 - (100/can) * (sayac-1)}")
        break
    elif sayi > tahmin:
        print("Yukari")
    else:
        print("Asaği")

    if hak == 0:
        print("Hakkiniz bitti: ")




