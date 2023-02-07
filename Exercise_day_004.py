#Day 4: 30 Days of python programming

print(".....................Question 1..............................................")
text = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(text)

print(".....................Question 2..............................................")
text = 'Coding' + ' ' + 'For' + ' ' + 'ALL' 
print(text)

print(".....................Question 3..............................................")
company = "Coding For All"
print(company)

print(".....................Question 4..............................................")
company = "Coding For All"
print(len(company))

print(".....................Question 5..............................................")
company = company.upper()
print(company)

print(".....................Question 6..............................................")
company = company.lower()
print(company)

print(".....................Question 7..............................................")
company = "Coding For All"
# capitalize the first character
capitalized_company = company.capitalize()
print(f"capitalize(): {capitalized_company}")
# format each word in the string as title case
title_company = company.title()
print(f"title(): {title_company}")
# swap the case of each character in the string
swapped_company = company.swapcase()
print(f"swapcase(): {swapped_company}")

print(".....................Question 8..............................................")
company = "Coding For All"
# slice the string starting from the index of the first space
first_word = company[:company.index(" ")]
print(f"First word: {first_word}")

print(".....................Question 9..............................................")
company = "Coding For All"
if company.find("Coding") != -1:
    print("The word 'Coding' is found in the string.")
else:
    print("The word 'Coding' is not found in the string.")

print(".....................Question 10..............................................")
company = "Coding For All"
company = company.replace("Coding", "Python")
print(company)

print(".....................Question 11..............................................")
company = "Python for Everyone"
company = company.replace("Everyone", "All")
print(company)

print(".....................Question 12..............................................")
company = "Coding For All"
words = company.split(" ")
print(words)

print(".....................Question 13..............................................")
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = companies.split(", ")
print(companies)

print(".....................Question 14..............................................")
company = "Coding For All"
first_char = company[0]
print(first_char)

print(".....................Question 15..............................................")
company = "Coding For All"
last_index = len(company) - 1
print(last_index)

print(".....................Question 16..............................................")
company = "Coding For All"
char_at_index_10 = company[10]
print(char_at_index_10)

print(".....................Question 17..............................................")
name = "Python For Everyone"
acronym = ""
words = name.split()
for word in words:
    acronym += word[0].upper()
print(acronym)

print(".....................Question 18..............................................")
name = "Coding For All"
words = name.split()
acronym = ""
for word in words:
    acronym += word[0].upper()
print(acronym)

print(".....................Question 19..............................................")
string = "Coding For All"
index = string.index("C")
print(index)

print(".....................Question 20..............................................")
string = "Coding For All"
index = string.index("F")
print(index)

print(".....................Question 21..............................................")
string = "Coding For All People"
last_occurrence = string.rfind('l')
print(last_occurrence)

print(".....................Question 22..............................................")
sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.find('because')
print(position)

print(".....................Question 23..............................................")
sentence = "You cannot end a sentence with because because because is a conjunction"
last_index = sentence.rindex("because")
print("The last occurrence of the word 'because' is at index", last_index)

print(".....................Question 24..............................................")
sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.find("because")
end = start + len("because because because")
phrase = sentence[start:end]

print(phrase)

print(".....................Question 25..............................................")
string = 'Coding For All'
result = string.startswith('Coding')
print(result)

print(".....................Question 26..............................................")
string = 'Coding For All'
result = string.endswith('Coding')
print(result)

print(".....................Question 27..............................................")
string = '   Coding For All      '
string = string.strip()
print(string)

print(".....................Question 28..............................................")
print ('''Which one of the following variables return True when we use the method isidentifier():
1. 30DaysOfPython
2. thirty_days_of_python''')

print ('''The variable "thirty_days_of_python" returns True when using the method isidentifier() because it is a valid Python identifier, consisting of lowercase letters and underscores, and starting with a lowercase letter.''')

print( '''The variable "30DaysOfPython" returns False because it starts with a number and is not a valid Python identifier.''')

print(".....................Question 29..............................................")
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
separator = "#"
joined_libraries = separator.join(libraries)
print(joined_libraries)

print(".....................Question 30..............................................")
print("I am enjoying this challenge.\nI just wonder what is next.")

print(".....................Question 31..............................................")
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

print(".....................Question 32..............................................")
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square".format(radius, area))

print(".....................Question 33..............................................")
print("8 + 6 = {}".format(8 + 6))
print("8 - 6 = {}".format(8 - 6))
print("8 * 6 = {}".format(8 * 6))
print("8 / 6 = {:.2f}".format(8 / 6))
print("8 % 6 = {}".format(8 % 6))
print("8 // 6 = {}".format(8 // 6))
print("8 ** 6 = {}".format(8 ** 6))

