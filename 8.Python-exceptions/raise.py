x = 10

if x > 5:
    raise Exception("x 5 den buyuk deger alamaz")


def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("paralo en az 8 karekter olmali")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola buyuk harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam harf içermelidir.")
    elif not re.search("[_@$$]", psw):
        raise Exception("parola alpha numerik karekter içermelidir.")
    elif re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("gecerli parola")


password = "123456789aB$"


try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("gecerli parola: else")
finally:
    print("validation tamamlandi.")