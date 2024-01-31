# global scope
x = 'global x'

def function():
    # local scope
    x = 'local x'
    print(x)

function() # ocal x
print(x) # global x

#--------------------------------------

# global
name = "Serhat"

def changeName(new_name):
    # local
    name = new_name
    print(name)


changeName("Ada") # Ada
print(name) # Serhat 

#--------------------------------------

name = "global string"

def greeting():
    name = "Cinar"

    def hello():
        print("hello " + name)

    hello()

greeting() # hello Cinar

#--------------------------------------

x = 50

def test():
    global x
    print(f"x {x}")

    x = 100
    print(f"changed x to {x}")

test(x) # 100
print(x) # 100