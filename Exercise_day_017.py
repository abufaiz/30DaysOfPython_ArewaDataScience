# Day 16 - 30DaysOfPython Exercises

print("......................... Q. 1.......................................")

names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# unpack the first five countries into a new list
nordic_countries = names[:5]

# store Estonia and Russia in separate variables
es, ru = names[-2:]

print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(es)  # 'Estonia'
print(ru)  # 'Russia'
