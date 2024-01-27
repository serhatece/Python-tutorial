if 3>2:       # True
    print("Welcome.") 

if 3<2:       # False
    print("Welcome.") 

if 3==3:       # True
    print("Welcome.") 

if True:       # True
    print("Welcome.") 

if False:       # False
    print("Welcome.") 



username = "serhatece"
password = "123456"

(username == "serhatece") and (password == "123456")

if (username == "serhatece"):
    if(password == "123456"):
        print("Giriş Başarili.")
    else:
        print("Paralo Yanliştir...")
else:
    print("Username Yanliştir...")