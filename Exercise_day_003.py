#Day 3: 30 Days of python programming

age = 35
height = 1.73
c = 1 +2j
print("My age is:", age)
print("My height is:", height)
print("The complex variable is:", c)


print("........................................................................")

base = float(input("Please enter the base of the triangle: "))
height = float(input("Please enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

print("........................................................................")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is:", perimeter)

print("........................................................................")
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

import math
print("........................................................................")
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)

print("........................................................................")
slope = 2
x_intercept = (1,0)
y_intercept = (0,-2)
print("The slope of the line is:", slope)
print("The x-intercept of the line is:", x_intercept)
print("The y-intercept of the line is:", y_intercept)

print("........................................................................")
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The slope of the line between the points is:", slope)
print("The Euclidean distance between the points is:", distance)

print("........................................................................")
print("The comparison between task 8 and 9 is :", 2 == 2)

print("........................................................................")
a = 1
b = 6
c = 9
x = (-b + math.sqrt(b**2 - 4*a*c))/(2*a) 
y = x**2 + 6*x + 9
print("The value of y when x =", x,"is:", y)

print("........................................................................")
string1 = 'python'
string2 = 'dragon'
length_string1 = len(string1)
length_string2 = len(string2)
print("The length of",string1,"is",length_string1)
print("The length of",string2,"is",length_string2)
if not length_string1 == length_string2:
    print("Length of",string1,"is not equal to the length of",string2)
else:
    print("Length of",string1,"is equal to the length of",string2)

print("........................................................................")
string1 = 'python'
string2 = 'dragon'
substring = 'on'
if (string1.find(substring) >= 0) and (string2.find(substring) >= 0):
    print("'on' is found in both",string1,"and",string2)
else:
    print("'on' is not found in both",string1,"and",string2)

print("........................................................................")
sentence = "I hope this course is not full of jargon."
word = "jargon"
if sentence.find(word) >= 0:
    print("The word",word,"is present in the sentence")
else:
    print("The word",word,"is not present in the sentence")

print("........................................................................")
text = "python"
length = str(float(len(text)))
print("The length of the text 'python' is:",length)

print("........................................................................")
num = 8.0
if num.is_integer() and num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

print("........................................................................")
import math
if 7 // 3 == math.floor(2.7):
    print("The floor division of 7 by 3 is equal to the floor value of 2.7")
else:
    print("The floor division of 7 by 3 is not equal to the floor value of 2.7")

print("........................................................................")
if type('10') == type(10):
    print("The type of '10' is equal to the type of 10")
else:
    print("The type of '10' is not equal to the type of 10")

print("........................................................................")
if int(math.floor(9.8)) == 10:
    print("int(math.floor(9.8)) is equal to 10")
else:
    print("int(math.floor(9.8)) is not equal to 10")

print("........................................................................")
hours = input("Enter the number of hours worked: ")
rate = input("Enter the rate per hour: ")
# convert the input to float
hours = float(hours)
rate = float(rate)
# calculate pay
pay = hours * rate
print("Pay: $" + str(pay))


print("........................................................................")
years = input("Enter the number of years a person can live: ")
# convert the input to float
years = float(years)
# calculate seconds
seconds = years * 365 * 24 * 60 * 60
print("Number of seconds a person can live: " + str(seconds))

print("........................................................................")
first_no = 1
second_no = 2
third_no = 3
forth_no = 4
fifth_no = 5
print(first_no, first_no **0, first_no **1, first_no **2, first_no **3)
print(second_no, second_no **0, second_no **2, second_no **3, second_no **3)
print(third_no, third_no **0, third_no **1, third_no **2, third_no **3)
print(forth_no, forth_no **0, forth_no **1, forth_no **2, forth_no **3)
print(fifth_no, fifth_no **0, fifth_no **1, fifth_no **2, fifth_no **3)

