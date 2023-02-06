#Day 2: 30 Days of python programming

first_name = 'Hassan'
last_name = 'Adamu'
full_name = 'Hassan Adamu'
country = 'Nigeria'
city = 'Hadejia'
age = 35
year = 1985
is_married = True
is_true = 'yes'
is_light_on = 'yes'
first_name, last_name, city = 'Hassan', 'Adamu', 'Hadejia'

print(".............Checking Data Types of the declared Variables............")
print (first_name, type ('Hassan'))
print (last_name, type ('Adamu'))
print (full_name, type ('Hassan Adamu'))
print (country, type ('Nigeria'))
print (city, type ('Hadejia'))
print (age, type (35))
print (year, type (1985))
print (is_married, type (True))
print (is_true, type ('yes'))
print (is_light_on, type ('yes'))
print (first_name, last_name, city, type('Hassan'))

print(".............Checking Length of First Name..............................")
print('First name length:', len(first_name))
print('Last name length:', len(last_name))

print(".......Calculating Some Mathematical Operators Using 5 and 4 as the values....")
num_one = 5 
num_two = 2
Total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print (Total)
print (diff)
print (product)
print (division)
print (remainder)
print (exp)
print (floor_division)

print(".............Checking Length of First Name..............................")
import math

radius = float(input("Please enter the radius of the circle: "))
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print("The circumference of the circle is:", circum_of_circle)
print("The area of the circle is:", area_of_circle)

print("............Using Input function to ask users their details..............")
first_name = input('Enter Your First Name: ')
last_name = input('Enter Your Last Name: ')
country = input('Enter Your Country: ')
age = input('How old are you? ')

print(first_name)
print(last_name)
print(country)
print(age)

help('for')
