# r+ = hem okuma hem yazma işlemini ifade eder

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(10)
#     file.write("deneme") # 10.cursorden sonra yazar.

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# ************** Sayfa Sonunda Guncelleme **************

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\n2.Satir") # dosyanın en sonuna yazar

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())


# ************** Sayfa Başında Guncelleme **************

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Guncelleme\n" + content
#     file.seek(0) 
#     file.write(content)
#     print(file.read())

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())


# ************** Sayfa Ortasında Guncelleme **************

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Serhat Yorulmaz")
    file.seek(0)
    for i in list:
        file.write(i)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
