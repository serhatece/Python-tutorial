# Identity Operator: is

x = y = [1,2,3]
z = [1,2,3]

print(x == y) # True
print(x == z) # True
print(x is y) # True
print(x is z) # False

a = [1,2,4]
b = [2,4]
print(x is y) # False

del x[2]
y[1] = 1
y.reverse()
print(x == y) # True
print(x is y) # False


# Membership Operator: in

c = ["apple","banana"]
print("banana" in c) # True

name = "Cinar"
print("a" in name) # True