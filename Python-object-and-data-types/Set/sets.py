fruits = {"orange","apple","banana"}

#! print(fruits[0]) # indexlenemez!!!!


for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape","apple"]) # apple oldugu ıcın elemanlar tekrarlanmaz.
print(fruits)

myList = [1,2,3,4,5,6,2,3,7,9]
print(myList)
print(set(myList)) # tekrar eden verıler lıste ıcınden gıder

fruits.remove("mango") # silme
fruits.discard("apple") # silme

fruits.pop() # herhangı bır elemanı sılebılır.
