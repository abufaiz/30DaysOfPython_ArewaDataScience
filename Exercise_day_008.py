#Day 8: 30 Days of python programming

print("...........................Exercise Level 1 (Q. 1)............................")
dog = {}
print(dog)

print("............................................(Q. 2)............................")
dog = {'color', 'breed', 'legs', 'age'}
print (dog)

print("............................................(Q. 3)............................")
student = {
    'first_name': 'Hassan',
    'last_name': 'Adamu',
    'gender': 'Male',
    'age': 35,
    'marital_status': 'Married',
    'skills': ['Python', 'Data Science', 'Machine Learning'],
    'country': 'Nigeria',
    'city': 'Hadejia',
    'address': 'No6 Gawuna Quarters'
}
print(student)

print("............................................(Q. 4)............................")
students_length = len(student)
print(students_length)

print("............................................(Q. 5)............................")
skills = student['skills']
print(skills)
print(type(skills))

print("............................................(Q. 6)............................")
student['skills'] = 'Data Visualization', 'SQL'
print(student['skills'])

print("............................................(Q. 8)............................")
student_keys = list(student.keys())
print(student_keys)

print("............................................(Q. 9)............................")
student_values = list(student.values())
print(student_values)

print("............................................(Q. 10)............................")
student_list = list(student.items())
print(student_list)

print("............................................(Q. 11)............................")
del student['address']
print(student)

print("............................................(Q. 11)............................")
del dog
