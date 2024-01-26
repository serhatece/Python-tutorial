salaryAli = 5000
salaryAhmet = 4000
tax = 0.27

print(salaryAli - (salaryAli * tax))
print(salaryAhmet - (salaryAhmet * tax))

#! Variable definition rules

#? cannot start with a number
number1 = 30  #true
#1number = 15  #false

#? It is case sensitive
yas = 20  #different
yaS = 18  #different

#? Let's not use Turkish characters
x = 1               # int
y = 2.3             # float
name = "Jack"       # string
#isStudent = true   # bool

# x,y,name,isStudent = (1,2.3,"Jack",true)

a = "20"
b = "30"
print(a+b) #30 => 2030

firstName = "Serhat"
lastName = " Ece"
print(firstName + lastName) # Serhat Ece