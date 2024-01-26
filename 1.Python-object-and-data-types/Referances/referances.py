# value types => string, numbers
x = 5
y = 25

x = y 

y = 10

#? y uzerınde yapılan degısıklık x'i etkilemedi
print(x,y) # 25 10

# referances types =>list

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b) # ["grape","banana"] ["grape","banana"] # her iki tarafta değişti