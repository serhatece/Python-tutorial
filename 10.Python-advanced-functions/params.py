def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a - b
def carpma(a,b):
    return a * b
def bölme(a,b):
    return a / b

def işlem(f1,f2,f3,f4,işlem_adi):
    if işlem_adi == "toplama":
        print(f1(2,3))
    elif işlem_adi == "cikarma":
        print(f2(5,3))
    elif işlem_adi == "carpma":
        print(f3(3,4))
    elif işlem_adi == "bölme":
        print(f4(20,2))
    else:
        print("Gecersiz İşlem...")


işlem(toplama,cikarma,carpma,bölme, "toplama") # 5
işlem(toplama,cikarma,carpma,bölme, "cikarma") # 2
işlem(toplama,cikarma,carpma,bölme, "carpma") # 12
işlem(toplama,cikarma,carpma,bölme, "bölme") # 10
işlem(toplama,cikarma,carpma,bölme, "mod-alma") # "Gecersiz İşlem..."
