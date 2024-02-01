# Yöntem 1
import math
import math as işlem

value = dir(math)
value2 = help(math)
value3 = help(math.factorial)

print(value)
print(value2)
print(value3)


result = math.sqrt(49) # 7
result = math.factorial(5) # 120
result = math.floor(5.9) # 5
result = math.ceil(5.9) # 6
result = işlem.factorial(5) # 120




# Yöntem 2
from math import *  # all
from math import factorial,sqrt # only this

deger = factorial(5) # 120
deger = sqrt(9) # 3
