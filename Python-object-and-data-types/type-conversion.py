x = input("1 = ") #10
y = input("2 = ") #20

total1 = x + y
print(type(x)) #str
print(type(y)) #str
print(total1) #1020

total2 = int(x) + int(y)
print(type(x)) #int
print(type(y)) #int
print(total2) #30


#!  Type Conversion

#? int to float
x = 10
x = float(x)
print(x)
print(type(x)) #float

#? float to int 
y = 2.25
y = int(y)
print(y)
print(type(y))

#? float to string
result = str(x) + str(y)
print(result)
print(type(result))

#? bool to string
isOnline = str(True)
print(isOnline)
print(type(isOnline))

#? bool to int 
isOnline = int(True)
print(isOnline) #1 true   #0 false
print(type(isOnline))
