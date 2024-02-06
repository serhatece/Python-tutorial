liste = [1,2,3,4,5]

# for i in liste:
#     print(i)

# print(dir(liste))


iterator = iter(liste)
print(iterator)

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5


while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break






class Mynumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
 
list = Mynumbers(10,20)

for x in list:
    print(x)
        # 10
        # 11
        # 12
        # 13
        # 14
        # 15
        # 16
        # 17
        # 18
        # 19
        # 20

myİter = iter(list)

print(next(myİter)) # 10
print(next(myİter)) # 11
print(next(myİter)) # 12
print(next(myİter)) # 13
print(next(myİter)) # 14

