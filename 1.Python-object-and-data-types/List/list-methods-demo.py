names = ["Ali","Yagmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
result = names.insert("Cenk")

# 2- "Sena" degerini listenin basina ekleyiniz.
result = names.insert(0,"Sena")

# 3- "Deniz" ismini listeden siliniz.
result = names.remove("Deniz")

# 4- "Deniz" isminin indeksi nedir ?
result = names.index("Deniz") #

# 5- "Ali" listenin bir elemani midir ?
result = "Ali" in names

# 6- Liste elemanlarin ters çevirin.
result = names.reverse

# 7- Liste elemanlarin alfabetik olarak siralayiniz.
result = names.sort()
result = years.sort()

# 8- years listesini rakamsal büyüklüge göre siralayin1z.
result = years.sort()

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye ceviriniz.
str = "Chevrolet, Dacia" 
result = str.split(",")

# 10- years dizisinin en büyük ve en küçük elemani nedir ?
result = min(years)
result = max(years)

# 11- years dizisinde kaç tane 1998 degeri vardir ?
result = years.count(1998)

# 12- years dizisinin tüm elemanlarin siliniz.
result = years.clear()

# 13- Kullanicidan alacaginiz 3 tane marka bilgisini bir listede saklayiniz.
markalar = []

marka = input("marka 1: ")
marka2 = input("marka 2: ")
marka3 = input("marka 3: ")
markalar.append(marka,marka2,marka3)
