# class

class Person:
    # class attributes
    address = "no information"

    # constructor (yapıcı metod)
    def __init__(self,name,year):

        # obect attributes
        self.name = name
        self.year = year
        
    # instance methods
    def intro(self):
        print("Hello There. I am " + self.name)

    # instance methods
    def calculateAge(self):
        return 2024 - self.year

# object  (instance)
p1 = Person("serhat",2003)
p2 = Person("ada",2001)

p1.intro()

# updating
p1.name = "Serhat"
p2.name = "Ada"
p1.address = "Bursa"
p2.address = "Ankara"


# accessing object attributes
print(f"name: {p1.name} year: {p1.year} yaşim: {p1.calculateAge} address: {p1.address}")
print(f"name: {p2.name} year: {p2.year} yaşim: {p2.calculateAge} address: {p2.address}")

print(p1 == p2) # False


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    

c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla} çevre = {c1.cevre_hesapla}")
print(f"c2 : alan = {c2.alan_hesapla} çevre = {c2.cevre_hesapla}")
