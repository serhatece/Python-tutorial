# BANKAMATİK UYGULAMASI

SerhatHesap = {
    "ad" : "Serhat Ece",
    "hesapNo" : "123456",
    "bakiye" : 3000,
    "ekHesap" : 2000
}
AdaHesap = {
    "ad" : "Ada Koyu",
    "hesapNo" : "654123",
    "bakiye" : 5000,
    "ekHesap" : 3000
}


def paraÇek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print("Paranizi alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanilsin mi? (e/h)")

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranizi alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
        else:
            print("Üzgünüz Bakiye Yetersiz..")
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadir.")

paraÇek(SerhatHesap,1500)
print("********************")
paraÇek(SerhatHesap,3000)