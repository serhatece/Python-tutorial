name = "Serhat Ece"

for letter in name:
    if letter == "e":
        continue
    print(letter)


x = 0

while x < 5:
    if x == 2:
        continue
    print(x)
    x += 1 


# 1-100 e kadar tek sayilarin toplami
    
y = 0
result  = 0
while y <= 100:
    y += 1
    if y % 2 == 0:
        continue
    result += y