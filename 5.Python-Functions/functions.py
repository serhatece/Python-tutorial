def sayHello1():
    print("Hello")

sayHello1()
sayHello1()
sayHello1()
#---------------------------------------------

def sayHello(name = "user"):
    print(f"Hello {name}")

sayHello("Serhat") # Hello Serhat
sayHello("Hakan") # Hello Hakan
sayHello() # Hello user
#---------------------------------------------

def sayHello2(name = "user"):
    return f"Hello {name}"

msg = sayHello2("Harun")
print(msg) # Hello Harun

msg1 = sayHello2("Ada")
print(msg1) # Hello Ada
#---------------------------------------------

def total(num1,num2):
    return num1 + num2


result = total(1+5)
print(result) # 6
#---------------------------------------------

def yasHesapla(dogumYili):
    return 2024 - dogumYili


ageSerhat = yasHesapla(2003)
print(ageSerhat) # 21
#---------------------------------------------

def emekiliğeKacYilKaldi(dogumYili,name):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emekiliğeKacYilKaldi > 0:
        print(f"emekililğinize {emeklilik} yil kaldi.")
    else:
        print("Zaten emekli oldunuz.")

emekiliğeKacYilKaldi(2003,"Serhat")