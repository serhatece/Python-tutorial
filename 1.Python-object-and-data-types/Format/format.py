name = "Jack"
surname = "Grealish"
age = 20 

print('My name is {}'.format(name))
print('My name is {0} {1}'.format(name,surname)) # Jack Grealish
print('My name is {1} {0}'.format(name,surname)) # Grealish Jack
print('My name is {n} {s} and I am {a} years ols'.format(n=name,s=surname,a=age))


result = 200 / 500
print('the result is {r}'.format(r=result)) # 0.285914....
print('the result is {r:1.3}'.format(r=result)) # 0.286


print(f'My name is {name} {surname} and I am {age} years ols')
