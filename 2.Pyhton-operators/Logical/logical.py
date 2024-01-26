x = 6
hak = 5
devam = "e"

result = 5 < x < 10 # False
result = 5 < x < 10 # True

#and
result = x > 5 and x < 10 # True,True => True
result = x > 7 and x < 10 # False,True => False

result = (hak > 0) and (devam == "e") # True,True => True

#or
result= (x < 0) or (x % 2 == 0) # False,True => True
result= (x > 0) or (x % 2 == 0) # True,True => True

#not
result = not(x > 0) # False

# x, 5-10 arasında olan bır cıft sayı mı?

result = ((x>5) and (x<10)) and (x%2 == 0) # True