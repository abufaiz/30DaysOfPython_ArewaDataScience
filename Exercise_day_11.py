#Day 11: 30 Days of python programming
print("...................Exercise Level 1 (Q.1).............................")

def add_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print(add_two_numbers(5,11))

print(".................................(Q.2)................................")
def area_of_circle(radius):
    pi = 3.14159265358979323846
    return pi * radius * radius
print(area_of_circle (5))

print(".................................(Q.3)................................")
def add_all_nums(*args):
    sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            sum += arg
        else:
            return "One of the arguments is not a number."
    return sum
print(add_all_nums(3,7))

print(".................................(Q.4)................................")
def convert_celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32
print(convert_celsius_to_fahrenheit(30))

print(".................................(Q.5)................................")
def check_season(month):
    if month >= 3 and month <= 5:
        return "Spring"
    elif month >= 6 and month <= 8:
        return "Summer"
    elif month >= 9 and month <= 11:
        return "Autumn"
    else:
        return "Winter"
print(check_season(4))

print(".................................(Q.6)................................")
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(15, 25, 40, 52))

print(".................................(Q.7)................................")
import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x,
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        return real + imag*1j, real - imag*1j
print(solve_quadratic_eqn(2,5,8))

print(".................................(Q.8)................................")
def print_list(input_list):
    for element in input_list:
        print(element)
#You can call this function by passing a list as an argument, for example
my_list = [1, 2, 3, 4, 5]
print_list(my_list)

print(".................................(Q.9)................................")
def reverse_list(input_list):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

print(".................................(Q.10)................................")
def capitalize_list_items(input_list):
    capitalized_list = []
    for item in input_list:
        capitalized_list.append(item.capitalize())
    return capitalized_list
#You can call this function by passing a list as an argument, for example:
print(capitalize_list_items(["apple", "banana", "cherry"]))
print(capitalize_list_items(["HELLO", "WORLD"]))

print(".................................(Q.11)................................")
def add_item(list, item):
    list.append(item)
    return list
#And then, you can use the function as follows:
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

print(".................................(Q.12)................................")
def remove_item(list, item):
    list.remove(item)
    return list
print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))

print(".................................(Q.13)................................")
def sum_of_numbers(number):
    return sum(range(1, number + 1))
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

print(".................................(Q.14)................................")
def sum_of_odds(number):
    return sum([x for x in range(1, number + 1) if x % 2 != 0])
print(sum_of_odds(5))
print(sum_of_odds(10))

print(".................................(Q.15)................................")
def sum_of_even(number):
    return sum([x for x in range(1, number + 1) if x % 2 == 0])
print(sum_of_even(100))
print(sum_of_even(10))

print("...................Exercise Level 2 (Q.1)..............................")
def evens_and_odds(number):
    evens = 0
    odds = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_and_odds(100))

print(".................................(Q.2)................................")
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
print(factorial(5))
print(factorial(10))
print(factorial(1))

print(".................................(Q.3)................................")
def is_empty(param):
    return len(param) == 0
print(is_empty(""))
print(is_empty("Hello World"))
print(is_empty([]))
print(is_empty([1, 2, 3, 4]))

print(".................................(Q.4................................")
import statistics

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_mode(numbers):
    return statistics.mode(numbers)

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std(numbers):
    return calculate_variance(numbers) ** 0.5

numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9]

print(calculate_mean(numbers))
print(calculate_median(numbers))
print(calculate_mode(numbers))
print(calculate_range(numbers))
print(calculate_variance(numbers))
print(calculate_std(numbers))


print("...................Exercise Level 3 (Q.1).............................")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime (2))

print(".................................(Q.2)................................")
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_all_items_unique([1, 2, 3, 4, 5]))
print(are_all_items_unique([1, 2, 3, 4, 5, 5]))

print(".................................(Q.3)................................")
def are_all_items_of_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)
print(are_all_items_of_same_type([1, 2, 3, 4, 5]))
print(are_all_items_of_same_type([1, 2, 3, 4, "5"]))

print(".................................(Q.4)................................")
import keyword
def is_valid_variable_name(name):
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True
print(is_valid_variable_name("_valid_variable_name"))
print(is_valid_variable_name("2invalid"))
print(is_valid_variable_name("for"))
print(is_valid_variable_name("validVariableName"))
print(".................................(Q.5)................................")
