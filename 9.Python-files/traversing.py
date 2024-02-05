with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0) # curso'u en başa goturur
    print(file.tell()) # cursor'un konumunu verır
