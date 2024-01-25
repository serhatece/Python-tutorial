website = "http://www.google.com"
course = "Python Course: Your Start-to-End Python Programming Guide (40 hours)"


#1- Delete the leading and trailing space characters of the 'Hello World' string.
result = " Hello World ".strip() # left-right
result = " Hello World ".ltrip() # left
result = " Hello World ".rtrip() # right

#2- Delete every character except the google information in 'http://www.google.com'.
result = "http://www.google.com".strip("w.moc") # delete

#3- Make all characters of the 'course' string lowercase.
result = course.lower() 
result = course.upper()
result = course.title()

#4- How many a characters are there in 'website'? (count('a'))
result = website.count("g") # 2

#5- Does 'website' start with www" and end with com?
result = website.startswith("www")

#6- Is there '.com' in 'website'?
result = website.find("com")

#7- Are the characters in 'course' all alphabetical? (isalpha, isdigit)
result = course.isalpha()

#8- Place the 'Contents' expression within 50 characters on the line and add * to the right and left.
result = "Contents".center(50)

#9- Replace all space characters in the 'course' string with '-'.
result = course.replace(" ", "-")

#10- Change 'World' to 'There' in the 'Hello World' string
result = "Hello World".replace("World", "There")

#11- Separate the 'course' string from the space characters.
result = course.split(" ")
