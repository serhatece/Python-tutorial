import random

result = dir(random)
result2 = help(random)

print(result)
print(result2)



value = random.random() # 0.0 - 1.0
value = random.uniform(1,10) # 1.0 - 10.0
value = random.uniform(10,100) # 10.0 - 100.0
value = int(random.uniform(10,100)) # 10 - 100
value = random.randint(1,10) # 1 - 10

print(value)



names = ["ali","ada","cenk","deniz"]

deger = names[random.randint(0,len(names)-1)]
deger = random.choice(names)

print(deger)


liste = list(range(10))
random.shuffle(liste) # elemanları karıstırır.

sonuc = liste

print(sonuc)