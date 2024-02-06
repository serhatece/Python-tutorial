# Üs Alma 

def usalma(number):
    def inner(power):
        return number ** power
    
    return inner

two = usalma(2)
three = usalma(3)
print(two(3)) # 2 üzeri 3 = 8
print(three(4)) # 3 üzeri 4 = 81





# Yetki Kontrol

def yetki_sorgula(page):
    def inner(role):
        if role == "Admin": 
            return f"{role} rolü {page} sayfasina ulaşabilir."
        else: 
            return f"{role} rolü {page} sayfasina ulaşamaz."
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("Admin")) # "Admin rolü Product Edit sayfasina ulaşabilir."

user2 = yetki_sorgula("Product Edit")
print(user2("User")) # "User rolü Product Edit sayfasina ulaşamaz."



# Carpma ve Toplama

def işlem(işlem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplama
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpma
    
    if işlem_adi == "toplama":
        return toplama
    else: 
        return carpma


top = işlem("toplama")
print(top(1,3,5,6,7)) # 22


carp = işlem("carpma")
print(carp(9,7)) # 63
