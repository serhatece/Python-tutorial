# 1-100 e kadar

x = 1

while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1


name = "" # False
while not name:
    name = input("isminizi giriniz")

print(f"Merhaba : {name}")