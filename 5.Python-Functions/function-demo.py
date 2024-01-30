# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaziniz.

def yazdir(kelime,adet):
    print(kelime*adet)

yazdir("Selam\n",10) # 10 kez
yazdir("Naber\n",5) # 5 kez
yazdir("Iyi\n",15) # 15 kez


# 2- Kendisine gönderilen sinirsiz sayidaki parametreyi bir listeye ceviren fonksiyonu yaziniz.

def listeyeCevir(*params):
    liste = []

    for param in params:
        list.append(param)

    return liste

result = listeyeCevir(10,20,30,"Selam")
print(result)

# 3- Gönderilen 2 sayi arasindaki tüm asal sayilari bulan fonksiyonu yaziniz.

def asalBul(s1,s2):
    for sayi in range(s1,s2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)


s1 = int(input("s1: "))
s2 = int(input("s2: "))

asalBul(s1,s2)

# 4- Kendisine gönderilen bir sayinin tam bölenlerini bir liste seklinde döndüren fonksiyonu yaziniz.

def tamBolenleriBul(number):
    tamBolenler = []

    for i in range(2,number):
        if(number % i == 0):
            tamBolenler.append(i)
    return tamBolenler

sonuc = tamBolenleriBul(20)
print(sonuc)
