def cube():
    for i in range(5):
        yield i ** 3

generator = cube()

iterator = iter(generator)

print(next(iterator)) # 0
print(next(iterator)) # 1
print(next(iterator)) # 8
print(next(iterator)) # 27
print(next(iterator)) # 64
print(next(iterator)) # StopIteration Error


for i in cube():
    print(i)




liste = (i ** 3 for i in range(5))
print(liste) # Generator Object


for i in liste():
    print(i)

print(next(liste)) # 0
print(next(liste)) # 1
print(next(liste)) # 8
print(next(liste)) # 27
print(next(liste)) # 64

