# 1- Girilen bir sayinin 0-100 arasinda olup olmadigini kontrol ediniz.
s1 = int(input("sayi: "))
result = (s1 >= 0) and (s1 <= 100)
print(result)

# 2- Girilen bir sayinin pozitif çift sayi olup olmadigini kontrol ediniz.
s2 = int(input("sayi: "))
result2 = (s2 >= 0) and (s2 % 2 == 0)
print(result2)

# 3- Email ve parola bilgileri ile giris kontrolü yapiniz.
email = "serhatece@gmail.com"
password = "123456"

email_giris = input("Email: ")
password_giris = input("Password: ")

result3 = (email == email_giris.lower()) and (password == password_giris.lower())

# 4- Girilen 3 sayıyı büyüklük olarak karsilastiriniz.
a1 = int(input("1.sayi: "))
b1 = int(input("2.sayi: "))
c1 = int(input("3.sayi: "))

a = (a1 > b1) and (a1 > c1)
b = (b1 > a1) and (b1 > c1)
c = (c1 > a1) and (c1 > b1)

print(f"a en buyuk mü? : {a}--- b en buyuk mü? : {b}--- c en buyuk mü? : {c}---")


# 5- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayiniz
#       Eger ortalama 50 ve üstündeyse gecti degilse kaldi yazdirin.
#           a-) Ortamalama 50 olsa bile final notu en az 50 olmalidir.
#           b-) Finalden 70 alindiginda ortalamanin önemi olmasin.

vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))  
final = float(input("final: "))

ort = (((vize1+vize2)/2) * 0.6) + (final * 0.4)
result = (ort >= 50) or (final >= 70)

print(f"ogr ORT: {ort} ve gecme durumu : {result}")


# 6- Kisinin ad, kilo ve boy bilgilerini alip kilo indekslerini hesaplayiniz.
#       Formül: (Kilo / boy uzunlugunun karesi)
#       Asagidaki tabloya göre kisi hangi gruba girmektedir.
#       0-18.4 => Zayif
#       18.5-24.9 => Normal
#       25.0-29.9 => Fazla Kilolu
#       30.0-34.9 => Sisman (Obez)
          
ad = input("ad: ")
kilo = float(input("kilo: "))
boy = float(input("boy: "))

kiloİndeks = (kilo) / (boy**2)

Zayif = (kiloİndeks > 0) and (kiloİndeks < 18.4)
Normal = (kiloİndeks > 18.5) and (kiloİndeks < 24.9 )
Fazla_Kilolu = (kiloİndeks > 25.0) and (kiloİndeks < 29.9)
Sisman = (kiloİndeks > 30.0) and (kiloİndeks < 34.9)

print(f"""
        ad: {ad}
        kilo: {kilo}
        boy: {boy}
        kilo indeksi: {kiloİndeks}
        Zayif: {Zayif}
        Normal: {Normal}
        Fazla Kilolu: {Fazla_Kilolu}
        Sisman (Obez): {Sisman}
""")
