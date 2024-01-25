# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarina sahip bir liste olusturunuz.
cars = ["Bmw", "Mercedes", "Opel", "Mazda"]
print(cars)

# 2- Liste Kaç elemanlidir ?
result = cars.count() # 4

# 3- Listenin ilk ve son elemani nedir ?
result = cars[0]
result = cars[-1]

# 4- Mazda degerini Toyota ile degistirin.
cars[-1] = "Toyota"
result = cars

# 5- Mercedes listenin bir eleman midir ?
result = "Mercedes" in cars # true
result = "1Mercedes" in cars # false

# 6- Listenin -2 indeksindeki deger nedir ?
result = cars[-2]

# 7- Listenin ilk 3 elemanini alin.
result = cars[:3]

# 8- Listenin son 2 eleman yerine "Totoya" ve "Renault" degerlerini ekleyin.
cars[-2:] = ["Toyota","Renault"]
result = cars

# 9- Listenin üzerine "Audi" ve "Nissan" degerlerini ekleyin.
result = cars + ["audi","nissan"]  

# 10- Listenin son elemanini silin.
del cars[-1]
result = cars

# 11- Liste elemanlarin tersten yazdiriniz.
result = cars[::-1]

# 12- Asagidaki verileri bir liste icinde saklayiniz.
    # studentA: Yigit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yigit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]


# 13- Liste elemanlarını yazdırınız.

result = studentA[0]
result = studentB[1]
result = studentC[3][2]

result = f"{studentA[0]} {[studentA[1]]} {2019-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
