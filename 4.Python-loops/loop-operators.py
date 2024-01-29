
#! Range()

for item in range(2,10):
    print(item)

for item in range(50,100,10):
    print(item) # 50,60,70,90

for item in range(50,100,20):
    print(item) # 50,20,90


#! enumerate
    
greeting = "Hello"

for index,letter in enumerate(greeting):
    print(f"letter : {letter} index: {index}")
    index += 1

for item in enumerate(greeting):
    print(item)


#! zip
    
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

print(list(zip(list1,list2)))

for item in zip(list1,list2):
    print(item)