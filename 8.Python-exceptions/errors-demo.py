liste = ["1", "2", "5a", "10b", "abc","10","50"]

# 1: Liste elemanlari içindeki sayisal degerleri bulunuz.

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

# 2: Kullanici 'q' degerini girmedikce aldiginiz her inputun sayi
#       oldugundan emin olunuz aksi halde hata mesaji yazin.

while True:
    sayi = input("sayi: ")
    if sayi == 'q':
        break

    try: 
        result = float(sayi)
        print("girdiğiniz sayi: " + result)
    except ValueError:
        print("geçersiz sayi")
        continue


# 3: Girilen parola icinde türkçe karakter hatasi veriniz.

def checkPassword(parola):
    turkce_karakterler = "şçğöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola turkce karakter içermez.")
        else: 
            pass
        print("geçerli parola")

parola = input("parola: ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)

# 4: Faktöriyel fonksiyonu olusturup fonksiyona gelen deger icin
#       hata mesajlari verin.


def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif Değer")

    result = 1

    for i in range(1,x+1):
        result *= i

    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)    