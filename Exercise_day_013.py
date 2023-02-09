#Day 13: 30 Days of python programming
print("....................................(Q.1).............................")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)

print("................................... (Q.2).............................")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flattened_list)


print("................................... (Q.3).............................")
#Using list comprehension create the following list of tuples:
#[(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
#(2, 1, 2, 4, 8, 16, 32),
#(3, 1, 3, 9, 27, 81, 243),
#(4, 1, 4, 16, 64, 256, 1024),
#(5, 1, 5, 25, 125, 625, 3125),
#(6, 1, 6, 36, 216, 1296, 7776),
#(7, 1, 7, 49, 343, 2401, 16807),
#(8, 1, 8, 64, 512, 4096, 32768),
#(9, 1, 9, 81, 729, 6561, 59049),
#(10, 1, 10, 100, 1000, 10000, 100000)]

list_of_tuples = [(x, 1, x**1, x**2, x**3, x**4, x**5) for x in range(11)]
print(list_of_tuples)


print("................................... (Q.4).............................")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [item for sublist in countries for item in sublist]
print(flattened_list)

print("................................... (Q.5).............................")
list_of_dicts = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(list_of_dicts)


print("................................... (Q.6).............................")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print(names)


print("................................... (Q.7).............................")
linear_eq = lambda x1, y1, x2, y2: ( (y2 - y1) / (x2 - x1), y1 - ( (y2 - y1) / (x2 - x1) ) * x1 )
print (linear_eq)