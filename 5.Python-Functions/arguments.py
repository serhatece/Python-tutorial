def changeName(n):
    n = "ada"

name = "serhat"

changeName(name)
print(name) # serhat


def change(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir"]

change(sehirler)
print(sehirler) # istanbul izmir
#-----------------------------------------------

def add(a,b,c = 0,d = 0,e = 0):
    return sum((a,b,c,d,e))

print(add(10,20)) # 30 
print(add(10,20,30)) # 60 
#-----------------------------------------------

def add1(*params):
    print(type(params)) # tuple
    return sum((params))

print(add1(10,20,30)) # 60 
print(add1(10,20,30,40)) # 100 
print(add1(10,20,30,40,50)) # 150 
print(add1(10,20,30,40,50,60)) # 210 
#-----------------------------------------------

def displayUser(**args):
    print(type(args)) # dict
    for key,value in args.items():
        print("{} is {}".format(key,value))

displayUser(name = "Serhat", age = 20,city = "Siirt")
displayUser(name = "Ada", age = 12,city = "London", phone = 123456789)
displayUser(name = "Yiğit", age = 41,city = "Ankara", phone = 987654321, email = "yiğit06@gmail.com")
#-----------------------------------------------

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1 = "value 1",key2 = "value 2")