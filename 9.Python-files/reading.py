try:
    file = open("newfile.txt","r")
    print(file)

except FileNotFoundError:
    print("dosya okuma hatasi")

finally:
    print("dosya kapandi")
    file.close()




file2 = open("newfile.txt","r",encoding="utf-8")

# for dongusu

for i in file:
    print(i, end="")

# read() fonksiyonu 
    
content = file2.read()
print(content)

result = file2.read(5) # ilk 5 karakter okur
result = file2.read(3) # 5 karakterden sonra 3 karakter okur
print(result)


# readline() fonksiyonu 

print(file.readline(),end="") # Her seferinde 1 satır okur
print(file.readline(),end="") # Her seferinde 1 satır okur
print(file.readline(),end="") # Her seferinde 1 satır okur
print(file.readline(),end="") # Her seferinde 1 satır okur


file2.close()