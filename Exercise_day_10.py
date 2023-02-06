#Day 10: 30 Days of python programming
print("...................Exercise Level 1 (Q.1).............................")
print(".................................While Loop...........................")
for i in range(11):
    print(i)
    
print(".................................While Loop...........................")
i = 0
while i < 11:
    print(i)
    i += 1

print(".................................(Q.2) for Loop.......................")
for i in range(10, -1, -1):
    print(i)

print(".................................While Loop...........................")
i = 10
while i >= 0:
    print(i)
    i -= 1

print(".................................(Q. 4)...............................")
# triangle
for i in range(1, 8):
    print('#' * i)

print(".................................(Q. 5)...............................")
for i in range(8):
    for j in range(16):
        if j % 2 == 0:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print('')

print(".................................(Q. 6)...............................")
for i in range(11):
    print(f"{i} x {i} = {i*i}")

print(".................................(Q. 7)...............................")
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in skills:
    print(item)

print(".................................(Q. 8)...............................")
for i in range(101):
    if i % 2 == 0:
        print(i)

print(".................................(Q. 9)...............................")
for i in range(101):
    if i % 2 != 0:
        print(i)

print("...................Exercise Level 2 (Q.1).............................")
sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers from 0 to 100 is:", sum)

print(".................................(Q. 2)...............................")
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
      odd_sum += i
print("The sum of all odd numbers from 0 to 100 is:", odd_sum)

print("...................Exercise Level 3 (Q.1).............................")
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)

print(".................................(Q. 2)...............................")


print(".................................(Q. 3)...............................")
