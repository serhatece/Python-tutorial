# key - value

# 41 => kocaeli 34 => İstanbul

sehirler = ["bursa","adana"]
plakalar = [16,1]

print(plakalar[sehirler.index("bursa")]) # 16
print(plakalar[sehirler.index("adana")]) # 1

#? example = {"key" : "value"}
plakalar = {"bursa":16, "adana":1}

print(plakalar["adana"]) # 16
print(plakalar["bursa"]) # 1

plakalar["value"] = "new value"



users = {
    "serhatece" : {
        "age" : 20,
        "roles" : ["admin","user"],
        "country" : "Turkey",
        "email" : "serhatece@gmail.com",
        "phone" : 5541789656
    },
    "cinarece" : {
        "age" : 17,
        "roles" : ["user"],
        "country" : "Germany",
        "email" : "cinarece@gmail.com",
        "phone" : 5526357496
    }
}

print(users["serhatece"]["age"])
print(users["serhatece"]["roles"][0])
print(users["serhatece"]["country"])
print(users["serhatece"]["email"])
print(users["serhatece"]["phone"])

print(users["cinarece"]["age"])
print(users["serhatece"]["roles"][0])
print(users["cinarece"]["country"])
print(users["cinarece"]["email"])
print(users["cinarece"]["phone"])
