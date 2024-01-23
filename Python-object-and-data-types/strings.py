name = "Serhat"
surname = "Ece"
age = 20

greeting  = 'My name is '+ name +' '+ surname + ' and \nI am '+str(age)+' years old'
length = len(greeting)

print(greeting)
print(greeting[0]) # M
print(greeting[1]) # y
print(greeting[2]) # 
print(greeting[3]) # n
print(greeting[4]) # a
print(greeting[5]) # m
print(greeting[6]) # e

print(len(greeting)) # 46
print(greeting[length-1]) # d
print(greeting[-1]) # d

print(greeting[3:7]) # name 

