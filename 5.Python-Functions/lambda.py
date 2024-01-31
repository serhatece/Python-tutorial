def square(num): return num ** 2

square = lambda num : num ** 2

numbers = [1,3,5,9]

result =  list(map(lambda num : num ** 2,numbers))
result =  list(map(square,numbers))
result = square(3)

print(result) # [1,9,25,81]

#--------------------------------------------------------------

number = [1,3,5,9,10,4]

def check_even(num1): return num1 % 2 == 0 

check = lambda num: num % 2 == 0

sonuc = list(filter(check_even,number))
sonuc = list(filter(lambda num: num % 2 == 0, number))
sonuc = list(filter(check,number))


print(sonuc) # 10,4

