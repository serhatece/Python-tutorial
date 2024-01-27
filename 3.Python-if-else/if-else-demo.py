# 1- Kullanicidan isim, yas ve egitim bilgilerini isteyip ehliyet alabilme
#       durumunu kontrol ediniz. Ehliyet alma kosulu en az 18 yas ve egitim durumu
#       lise ya da üniversite olmalidir.

isim = input("isim: ")
yas = int(input("yaş: "))
egitim = input("egitim : ")

if (yas >= 18):
    if(egitim.lower() == "lise"):
        print("Tebrikler Ehliyet alabilirsiniz.")
    elif(egitim.lower() == "üniversite"):
        print("Tebrikler Ehliyet alabilirsiniz.")
    else:
        print("egitim durumu lise ya da üniversite olmalidir.")
else:
    print("Yaşiniz 18'den küçük olamaz.")

# ----------------------------------------------------------------------------------------
    
# 2- Bir ögrencinin 2 yazili bir sözlü notunu alip hesaplanan ortalamaya göre
#       not araligina karsilik gelen not bilgisini yazdirinz.
# 0 -24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5
    
yazili1 = float(input("yazili 1: "))
yazili2 = float(input("yazili 2: "))
sozlü = float(input("sözlü: "))

ort = (yazili1+ yazili2+sozlü)/3

if (ort > 0):
    if(ort <= 24):
        print(f"Ortalamaniz {ort} Not Bilginiz: 0")
    elif(ort <= 44):
        print(f"Ortalamaniz {ort} Not Bilginiz: 1")
    elif(ort <= 54):
        print(f"Ortalamaniz {ort} Not Bilginiz: 2")
    elif(ort <= 69):
        print(f"Ortalamaniz {ort} Not Bilginiz: 3")
    elif(ort <= 84):
        print(f"Ortalamaniz {ort} Not Bilginiz: 4")
    if(ort <= 100):
        print(f"Ortalamaniz {ort} Not Bilginiz: 5")
else:
    print("Ortalamaniz 0'dan düşük.")

# ----------------------------------------------------------------------------------------

# 3- Trafige cikis tarihi alinan bir aracin servis zamanini asagidaki bilgilere
#       göre hesaplayin1z.
# 1. Bakim => 1. yil
# 2. Bakim => 2. yil
# 3. Bakim => 3. yil
#   Süre hesabini alinan gün, ay, yil bilgisine göre gün bazli hesaplayiniz
#       datetime modülünü kullanmaniz gerekiyor.

import datetime

tarih = int(input("Araciniz hangi tarihte trafiğe çikti (2024/01/27): "))
tarih = tarih.split("/")

trafiğeCikis = datetime.datetime(int(tarih[0],tarih[1],tarih[2]))
now = datetime.datetime.now()
fark = now - trafiğeCikis
days = fark.days


if days <= 365:
    print("1.servis araliği")
elif days > 365 and days <= 365 * 2:
    print("2.servis araliği")
elif days > 365*2 and days <= 365 * 3:
    print("3.servis araliği")
else:
    print("Hatali süre.")
