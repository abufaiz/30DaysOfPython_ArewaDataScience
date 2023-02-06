#Day 7: 30 Days of python programming

print("...........................Exercise Level 1 (Q. 1)............................")
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
length = len(it_companies)
print("The length of the set is:", length)

print("............................................(Q. 2)............................")
it_companies.add('Twitter')
print("The set after adding Twitter:", it_companies)

print("............................................(Q. 2)............................")
it_companies.update(['FlexiSAF', 'Instagram', 'Tik Tok', 'SanhaTech', 'Microsoft'])
print(it_companies)

print("............................................(Q. 3)............................")
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
del it_companies

print("............................................(Q. 4)............................")
print('''In Python, both remove and discard methods are used to remove elements from a set (a collection of unique elements).
The difference between the two methods lies in how they behave when trying to remove an element that does not exist 
in the set.

Therefore, it is recommended to use discard when you want to remove an element from a set
and do not care about raising an error if the element does not exist. On the other hand,
you should use remove if you want to ensure that the element you are trying to remove is in the set''')

print("...........................Exercise Level 2...................................")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("............................................(Q. 1)............................")
C = A.union(B)
print (C)

print("............................................(Q. 2)............................")
D = A.intersection(B)
print (D)

print("............................................(Q. 3)............................")
E = A.isdisjoint(B)
print (E)

print("............................................(Q. 4)............................")
# Find the union of sets A and B
F = A.union(B)
# Find the union of sets B and A
G = B.union(A)
# Print the results
print("Union of sets A and B:", F)
print("Union of sets B and A:", G)

print("............................................(Q. 5)............................")
H = A.symmetric_difference(B)
print(H)

print("............................................(Q. 6)............................")
# Delete set A
del A
# Delete set B
del B

print("......................................Exercises: Level 3......................")

print("............................................(Q. 6)............................")
ages = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the list of ages to a set
unique_ages = set(ages)
# Compare the length of the list and the set
print("Length of the list:", len(ages))
print("Length of the set:", len(unique_ages))

print("............................................(Q. 6)............................")
print ('''Strings: Strings are sequences of characters and are used to represent text data. They are defined using single quotes (') or double quotes ("). Strings are immutable, which means that you cannot modify individual characters within a string after it has been created.

Lists: Lists are ordered, mutable sequences of elements. You can add, remove, or modify elements within a list after it has been created. Lists are defined using square brackets ([]).

Tuples: Tuples are also ordered sequences of elements, but unlike lists, they are immutable. Once a tuple is created, you cannot modify its elements. Tuples are defined using parentheses (()).

Sets: Sets are unordered collections of unique elements. Sets are similar to lists and tuples, but unlike these data types, sets do not allow duplicates. Sets are defined using curly braces ({}).''')

print("............................................(Q. 6)............................")
sentence = "I am a teacher and I love to inspire and teach people."
# Split the sentence into words
words = sentence.split(" ")
# Create a set of unique words
unique_words = set(words)
# Count the number of unique words
count = len(unique_words)
# Print the result
print("Number of unique words:", count)
