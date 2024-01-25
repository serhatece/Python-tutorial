"""
    ogrenciler = {
        '120' : {
            'ad': 'Ali',
            'soyad': 'Yilmaz',
            'telefon' : '532 000 00 01'
        },
        '125' : {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon' : '532 000 00 02'
        },
        '128' : {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon' : '532 000 00 03'
        },
    }

    1- Bilgileri verilen ögrencileri kullanicidan aldigniz bilgilerle
        dictionary içinde saklayiniz.

    2- Ögrenci numarasini kullanicidan alip ilgili ögrenci bilgisini gösterin.
"""

ogrenciler = {}

number = input("Ogr no: ")
name = input("Ogr adi: ")
surname = input("Ogr soyad: ")
phone = input("Ogr tel: ")

ogrenciler[number] = {
    "ad": name,
    "soyad" : surname,
    "phone" : phone
}

ogrenciler.update({
    number : {
        "ad" : name,
        "surname" : surname,
        "phone" : phone
    }
})


print(ogrenciler)



ogrNo = input("ogrenci no : ")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)