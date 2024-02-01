import mod

result = help(mod)
result = help(mod.func)
result = mod.number # 10
result = mod.numbers # 10
result = mod.person["name"]
result = mod.person["age"]
result = mod.person["city"]
result = mod.func(10) # x: 10
 
print(result)

p = mod.person()
p.speak()
