# Dosya açmak ve olusturmak için open() fonksiyonu kullanilir.
# Kullanimi: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyayi hangi amaçla actigimizi belirtir.

# "w": (Write) yazma modu. 
#       Dosyayi konumda olusturur.
#       Dosya içeriğini siler ve yeniden ekleme yapar.

file = open("newfile.txt","w",encoding="utf-8")
file.write("Serhat Ece")
file.close()


# "a": (Append) ekleme. Dosya konumda yoksa olusturur.

file2 = open("newfile2.txt","a",encoding="utf-8")
file2.write("Serhat Ece")
file2.close()

# "x": (Create) olusturma. Dosya zaten varsa hata verir.

file3 = open("newfile3.txt","x",encoding="utf-8")

# "r": (Read) okuma. varsayilan. dosya konumda yoksa hata verir.