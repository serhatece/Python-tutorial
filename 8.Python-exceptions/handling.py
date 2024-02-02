# error handling => hata yönetimi

try:
    x = int(input("x: " ))
    y = int(input("y: " ))
    print(x/y) 

except (ZeroDivisionError,ValueError) as e:
    print("yanliş bilgi girdiniz.")
    print(e)



try:
    x = int(input("x: " ))
    y = int(input("y: " ))
    print(x/y) 

except:
    print("yanliş bilgi girdiniz.")

else:
    print("Hersey yolunda:)")



while True:
    try:
        x = int(input("x: " ))
        y = int(input("y: " ))
        print(x/y) 

    except Exception as ex:
        print("yanliş bilgi girdiniz.", ex)

    else:
        break

    finally:
        print("try expect sonlandi.")