"""
Soru: Girilen bir sayinin asal olup olmadigini bulun.
** Asal Sayi 1 ve kendisi haric tam böleni olmayan
    sayilara denir.

"""

sayi = int(input("Sayi: "))
asalMi = True

if sayi < 2:
    asalMi = False
elif sayi == 2:
    asalMi = True
else:
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            asalMi = False
            break

if asalMi:
    print("Sayi asaldir.")
else:
    print("Sayi asal değildir.")