# Inheritance (Kalıtım): Miras alma

# Person => name,lastname,age,eat(),kos(),drink()

# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print("Person Created")

    def who_am_i(self):
        print("I am the Person")


    def eat(self):
        print("I am eating.")


class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print("Student Created")

    # override
    def who_am_i(self):
        print("I am the Student")

    def sayHello(self):
        print("Hello I am a Student")


class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Serhat","Ece")
s1 = Student("Serhat","Ece",24)
t1 = Teacher("Jack","Allow","Math")

t1.who_am_i()

print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNumber))

