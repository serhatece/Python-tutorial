website = "http://www.google.com"
course = "Python Course: Your Start-to-End Guide to Python Programming (40 hours)"


#? 1- How many characters are there in the character string 'course'?
length = len(course) # 65
length2 = len(website)

#? 2- Get www characters from 'website'.
get = website[7:10] # www

#? 3- Get com characters from 'website'.
get2 = website[22:25] # com
get3 = website[length2-3:length2] # com


#? 4- Get the first 15 and last 15 characters from 'course'.
get4 = website[:15]
get5 = website[-15:]

#? 5- Reverse the characters in the 'course' expression.
get6 = course[::-1]


name, surname, age, job = 'Bora', 'Vilmaz', 32, 'Engineer'

#? 6- Print the following expression on the screen with the variables given above.
#       'My name is Bora Yilmaz, I am 32 years old and my profession is engineer.'

result = f"My name is {name} {surname}, I am {age} years old and my profession is {job}."

#? 7- Replace the letter w in the phrase 'Hello world' with 'W'.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]

#? 8- Print the phrase 'abc' side by side 3 times.

get7 = " abc " * 3
print(get7)