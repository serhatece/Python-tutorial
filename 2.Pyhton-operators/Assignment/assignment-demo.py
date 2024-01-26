x,y,z = 2,5,107

numbers = 1,5,7,10,6



# 1- Kullanicidan aldiganiz 2 sayinin carpimi ile x,y,z toplaminin farki nedir
s1 = int(input("1.sayi: "))
s2 = int(input("2.sayi: "))
fark = (s1*s2) - (x+y+z)
print(fark)

# 2- y' nin x' e kalansiz bölümünü hesaplayinz.
result = y // x # "//" kalansız bolme

# 3- (x,y,z) toplaminin mod 3' ü nedir ?
result = (x+y+z) % 3

# 4- y' nin x. kuvvetini hesaplayiniz.
result = y ** x

# 5- x, *y, z = numbers islemine göre z' nin küpü kaçtir ?
x,*y,z = numbers
result = z ** 3 # 216

# 6- x, *y, z = numbers islemine göre y nin degerleri toplami kaçtir ?
x,*y,z = numbers
result = y[0] + y[1] + y[2] # 22

