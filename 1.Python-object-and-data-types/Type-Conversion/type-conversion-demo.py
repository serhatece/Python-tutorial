"""
    Circle Area: πr2
    Circle Circumference: 2πr 
    * Area and perimeter of a circle given its radius
    Calculate. (r : 3.14)
"""

#? Given radius
pi = 3.14
r = float(input("radius:  "))

#? Calculate area and circumference
circle_area = pi * (r ** 2)
print(type(circle_area)) #float
circle_circumference = 2 * pi * r
print(type(circle_circumference)) #float

#? Print the results
print("Circle Area:", str(circle_area))
print("Circle Circumference:", str(circle_circumference))
