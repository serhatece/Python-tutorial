my_list = [1,2,3]
my_list = ["1",2,True,5.6]

print(my_list)
#-----------------------------------
list = ["one","two","there"]
list2 = ["four","five","six"]

numbers = list + list2
print(numbers)
print(len(numbers)) # 6 
#-----------------------------------
userA = ["Serhat",20]
userB = ["Çinar",27]

users = [userA + userB]

print(userA)
print(userB)
print(users)
print(users[0][0]) # Serhat
print(users[0][1]) # 20
print(users[1][0]) # Çinar
print(users[1][1]) # 27

