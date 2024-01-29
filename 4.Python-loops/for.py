numbers = [1,2,3,4,5]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])


for num in numbers:
    print(num)


names = ["cinar","sadik","serhat"]

for name in names:
    print(f"My name is: {name}")


name = "Serhat Ece"

for n in name:
    print(n)


tuple = [(1,2,3),(4,5)]

for t in tuple:
    print(t) 


d = {"k1" :1, "k2" :2, "k3" :3}

for item in d:
    print(item) # k1,k2,k3

for key,value in d.items():
    print(key,value)