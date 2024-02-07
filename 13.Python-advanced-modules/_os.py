import os
import datetime

# result = dir(os)
# result = os.name # nt = Windows

#? Dizin Değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

#? Klasor Olusturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör") # Dosyada Yeni klasor olusturma
# os.rename("newdirectory","yeni_ad_klasor") # Klasor ismi değiştirme
# os.rmdir("newdirectory") # Klasors silme
# os.removedirs("yeniklasör/yeniklasör")

#? Etkin Dizini Öğrenme
# result = os.getcwd # Klasorun nerde oldugunu yazar

#? Listeleme
# result = os.listdir() # Klasorlerı Listeler


# result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihi


# os.system("notepad.exe")

# print(result) 






#! Path
#*  Uzantılar ile ilgili İşlemlerde Kullanılır 


sonuc = os.path.abspath("_os.py") # Dosya Yolunu verir.
sonuc = os.path.exists("_os.py") # Dosya'nın olup olmadıgını kontrol eder ve True=False deger gonderır



print(sonuc)