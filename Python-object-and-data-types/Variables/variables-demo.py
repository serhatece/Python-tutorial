"""
1- Create a variable for the following information of a customer.
    Customer name
    Customer surname
    Customer name + surname
    Customer gender
    Customer TR ID
    Customer birthday year
    Customer address information
    Customer age
"""
#? Customer information variables
customer_name = "John"
customer_surname = "Doe"
customer_full_name = customer_name + " " + customer_surname
customer_gender = "Male"
customer_id_number = "12345678900"
customer_birth_year = 1990
customer_address = "Sample Address, Sample City"
customer_age = 2024 - customer_birth_year

#? Print customer information
print("Customer Name:", customer_name)
print("Customer Surname:", customer_surname)
print("Customer Full Name:", customer_full_name)
print("Customer Gender:", customer_gender)
print("Customer ID Number:", customer_id_number)
print("Customer Birth Year:", customer_birth_year)
print("Customer Address:", customer_address)
print("Customer Age:", customer_age)


"""
    2- Calculate the total information of the following orders.
    Order 1 => 110 TL
    Order 2 => 1100.5 TL
    Order 3 => 356.95 TL
"""
#? Order information
order1_amount = 110
order2_amount = 1100.5
order3_amount = 356.95

#? Calculate total amount
total_amount = order1_amount + order2_amount + order3_amount

#? Print the total amount
print("Total Amount of Orders:", total_amount)
