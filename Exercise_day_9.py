#Day 9: 30 Days of python programming
print("...........................Exercise Level 1 (Q. 1)............................")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    wait_time = 18 - age
    print(f"You need to wait for {wait_time} years to be able to drive.")
    
print("............................................(Q. 2)............................")
my_age = 38
your_age = int(input("Enter your age: "))

if my_age == your_age:
    print("We are the same age.")
elif my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
else:
    age_difference = your_age - my_age
    if age_difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")


print("............................................(Q. 3)............................")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")


print("............................................(Q. 4)............................")
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


print("............................................(Q. 5)............................")
month = input("Enter a month: ")

if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month.")


print("............................................(Q. 6)............................")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("The modified list is:", fruits)
    

print("...........................Exercise Level 2 (Q. 1)............................")
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("The middle skill is:", skills[middle_index])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has the 'Python' skill.")
    else:
        print("The person does not have the 'Python' skill.")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer.")
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print("He is a backend developer.")
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

# If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], "is married and lives in", person['country'])
