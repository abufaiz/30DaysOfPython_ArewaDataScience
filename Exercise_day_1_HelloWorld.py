# Day 1 - 30DaysOfPython Exercises 
# Exercise Level 2

print("...................(""Exercise Level 1 and 2"")............................")
# Question 1 - Check the python version you are using
import sys
print (sys. version)


# Question 2 - Calculating mathematical operator uding 3 and 4 operands 
print("....................('Mathematical Operators in Python')...........")
print(3 + 4)             
print(3 - 4)             
print(3 * 4)            
print(3 / 2)             
print(3 ** 4)
print(3 % 4)             
print(3 // 4)            


# Question 3 - Write strings on the python interactive shell.
#The strings are the following:
print(".............('Write strings on the python interactive shell').....")
print("....................('Sring').....................................")
print ("Hassan")
print ("Adamu")
print ("Nigeria")
print ("I am enjoying 30 days of python")


# Question 4 - Checking data types
print("....................('Checking Data types').......................")
print(type(10))          
print(type(3.14))        
print(type(4 + 4j))      
print(type(['Asabeneh', 'Python', 'Finland']))  
print(type('Hassan')) 
print(type('Adamu')) 
print(type('Nigeria'))    

print("...................(""Exercise Level 3"")............................")

# Exercise Level 3

print("..........The following are examples of different data types..........///////")
# Ineteger Data type
print("....................('INTEGER DATA TYPE').....................................")
a = 5
print(a)

print("....................('FLOAT DATA TYPE').....................................")
# Float Data type
b = 5.2
print(b)

print("....................('COMPLEX DATA TYPE').....................................")
c = 2 + 4j
print(c)

print("....................('STRING DATA TYPE').....................................")
a = 'Arewa Data Science Fellewship'
print(a)  

b = 'Thirty Days Of Python Challenge'
print(b)

print("....................('LIST DATA TYPE').....................................")
# List Data type 
# access of items in the list as index 0 - 2 because the items are 3
Nigerian_Major_languages = ["Hausa", "Yoruba", "Igbo"]
print(Nigerian_Major_languages[0])  
print(Nigerian_Major_languages[1]) 
print(Nigerian_Major_languages[2])  

print("....................('TUPLE DATA TYPE').....................................") 

# Tuple Data type 
# I used index number just like in the list to access items in python 
dishes = ('Fried Rice', 'Chicken Biryani', 'Nasi Gorneg Ayam Tumyit')
print(dishes[0])  
print(dishes[1]) 
print(dishes[2])   

print("....................('SET DATA TYPE').....................................")
# I created a set named student_id
student_id = {112, 114, 116, 118, 115}
# This display student_id elements
print(student_id)

print("....................('DICTIONARY DATA TYPE')...............................")
# I created a dictionary named Nigeria which contains the states under the 3 Northern region
nigeria = {'North_west': 'Jigawa', 'North_east': 'Borno', 'North_central': 'Kaduna'}
print(nigeria['North_west']) 
print(nigeria['North_east'])
print(nigeria['North_central'])   

print(".........Finding Euclidian distance between (2, 3) and (10, 8).............")
import math
x = (2, 3)
y = (10, 8)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("The Euclidean distance from x = (2, 3) to y = (10, 8): ",distance)


