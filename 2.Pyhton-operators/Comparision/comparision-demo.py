# 1- Girilen 2 sayidan hangisi büyüktür ?
s1 = int(print("1.sayi = "))
s2 = int(print("2.sayi = "))

result = (s1 > s2)
print(f"s1:{s1} s2:{s2} den buyuktur: {result}")

# 2- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayin1z
#       Eger ortalama 50 ve üstündeyse gecti degilse kaldi yazdirin.
vize1 = float(input("vize 1: "))
vize2 = float(input("vize 2: "))
final = float(input("final : "))
ort = (((vize1+vize2)/2) * 0.6) + (final * 0.4)

# 3- Girilen bir sayinin tek mi cift mi oldugunu yazdirin.
sayi = int(input("sayi: "))
tekcift = (sayi % 2 == 0)


# 4- Girilen bir sayinin negatif pozitif durumunu yazdirin.
sayi1 = int(input("sayi: "))
pozitifmi = (sayi > 0)

# 5- Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
#       (email: email@sadikturan.com parola: abc123)

email = "email@serhatece.com "
password = "abc123"

girilenEmail = input("e-mail: ")
girilenPassword = input("parola: ")

isEmail = (email == girilenEmail.lower()) # kucuk harfe cevırır.
isPassword = (password == girilenPassword.lower())

print(f"Email dogrumu : {isEmail} ve Parola dogru mu : {isPassword}")