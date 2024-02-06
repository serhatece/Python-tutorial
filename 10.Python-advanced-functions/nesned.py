def greeting(name):
    print("hello ", name)

print(greeting("serhat"))
print(greeting)

sayHello = greeting

print(sayHello) # Aynı adres
print(greeting) # Aynı adres

del sayHello
print(greeting) # Adres aynı gene 



#! Encapsulation

def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1 , num2)

outer(10)


#! Faktoriyel Hesaplama

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    
    if not number >= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:  
            return 1
        
        return number * inner_factorial(number - 1)
    return inner_factorial(number)


print(factorial(5)) # 120
print(factorial(4)) # 24
print(factorial(6)) # 720
print(factorial("a")) # TypeError = "number must be an integer"
print(factorial(-2)) # ValueError = "number must be zero or positive"



