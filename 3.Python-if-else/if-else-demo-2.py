"""
1- Girilen bir sayinin 0-100 arasinda olup olmadigini kontrol ediniz.

"""
sayi = int(input("sayi: "))
if (sayi > 0 and sayi <= 100):
    print("sayi 0 ile 100 arasnda")
else:
    print("Sayi 0 ile 100 arasinda değil")


"""
2- Girilen bir sayinin pozitif cift sayi olup olmadigini kontrol ediniz.

"""

s1 = int(input("s1: "))

if(s1 > 0):
    if(s1 % 2 == 0):
        print("Sayi pozitif ve çift bir sayidir.")
    else:
        print("Sayi pozitif ve tek bir sayidir.")
else:
    print("Sayi negatifdir.")


"""

3- Girilen 3 sayiyi büyüklük olarak karsilastiriniz.

"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a > b) and (a > c):
    print("a en buyük sayidir.")
elif (a == b) and (a == c) and (b == c):
    print("Tüm sayilar eşittir")
elif (b > a) and (b > c):
    print("b en büyük sayidir.")
else:
    print("c en büyük sayidir.")