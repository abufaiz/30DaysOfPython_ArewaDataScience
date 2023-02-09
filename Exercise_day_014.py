#Day 14: 30 Days of python programming
print("....................Exercise Level 1 (Q.1).............................")

print('''Map: "Map" takes an array as input, applies a function to each element 
       of the array, and returns a new array with the results. The new array 
       will have the same number of elements as the original array. For example, 
       you could use "Map" to square each element in an array of numbers.''')

print('''Filter: "Filter" takes an array as input and returns a new array that 
      contains only the elements of the original array that meet certain criteria 
      specified in the function passed to "Filter". For example, you could use 
      "Filter" to extract all even numbers from an array of numbers.''')

print('''Reduce: "Reduce" takes an array as input, applies a function to each 
      element of the array (in a cumulative manner), and returns a single value 
      as output. The function passed to "Reduce" takes two arguments: an accumulator
      (which starts as the first element of the array) and the current element 
      being processed. The accumulator is updated for each iteration and its 
      final value is returned as the result. For example, you could use "Reduce" 
      to find the sum of all elements in an array of numbers.''')
      
print(".....................................(Q.2).............................")
print('''Higher-Order Functions: A higher-order function is a function that takes 
      one or more functions as arguments and/or returns a function as its result.
      Higher-order functions are a fundamental concept in functional programming 
      and are used to abstract and reuse common operations on functions.''')

print(''''Closures: A closure is a function object that has access to variables in 
      its enclosing scope even after the outer function has returned. A closure 
      allows a function to "remember" its lexical scope even when it's invoked 
      outside that scope. In other words, a closure is a function that remembers 
      values in the scope in which it was created even if you access them in a 
      different scope.''')

print('''Decorators: A decorator is a special kind of function or construct in 
      Python (and other programming languages) that allows you to modify or extend 
      the behavior of another function or object without having to modify the 
      source code of the original function. A decorator takes a function as its
      input, extends or modifies its behavior, and returns a new function that can
      replace the original. Decorators are often used to add or remove 
      functionality to existing functions, such as adding logging, performance
      measurement, or authentication.''')


print(".....................................(Q.3).............................")
#Here's an example of a simple callable in Python
class Multiply:
    def __init__(self, factor):
        self.factor = factor
        
    def __call__(self, value):
        return self.factor * value

multiply_by_2 = Multiply(2)
print(multiply_by_2(5)) # 10


#Here's how you could use a callable with the map function:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(multiply_by_2, numbers)
print(list(squared_numbers)) 

#Similarly, you could use a callable with the filter function:
def is_even(value):
    return value % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers)) 

#Finally, you could use a callable with the reduce function:
from functools import reduce
def add(accumulator, value):
    return accumulator + value
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers) 

print(".....................................(Q.4).............................")
countries = ['Nigeria', 'USA', 'Canada', 'Mexico', 'Brazil', 'Argentina']
for country in countries:
    print(country)

print(".....................................(Q.5).............................")
names = ['Hassan', 'Hussaini', 'Adnan', 'Faiz', 'Fatima']
for name in names:
    print(name)


print(".....................................(Q.6).............................")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

print("....................Exercise Level 2 (Q.1).............................")
countries = ['Nigeria', 'USA', 'Canada', 'Mexico', 'Brazil', 'Argentina']
def to_uppercase(country):
    return country.upper()
uppercase_countries = list(map(to_uppercase, countries))
print(uppercase_countries)

print(".....................................(Q.6).............................")
num = [1, 2, 3, 4, 5]
def square(number):
    return number * number
squared_num = list(map(square, num))
print(squared_num)

print(".....................................(Q.6).............................")
#names = ['Hassan', 'Hussaini', 'Adnan', 'Faiz', 'Fatima']
def to_uppercase(name):
    return name.upper()
uppercase_names = list(map(to_uppercase, names))
print(uppercase_names)

print(".....................................(Q.6).............................")
countries = ['Iceland', 'Finland', 'Switzerland', 'Thailand', 'Ireland']
def has_land(country):
    return 'land' in country
land_countries = list(filter(has_land, countries))
print(land_countries)

print(".....................................(Q.6).............................")
countries = ['France', 'Germany', 'Italy', 'Spain', 'Greece']
def has_six_chars(country):
    return len(country) == 6
six_char_countries = list(filter(has_six_chars, countries))
print(six_char_countries)

print(".....................................(Q.6).............................")
countries = ['France', 'Germany', 'Italy', 'Spain', 'Greece']
def has_six_or_more_chars(country):
    return len(country) >= 6
six_or_more_char_countries = list(filter(has_six_or_more_chars, countries))
print(six_or_more_char_countries)

print(".....................................(Q.6).............................")
countries = ['France', 'Germany', 'Italy', 'Spain', 'Greece']
def starts_with_e(country):
    return country[0] == 'E'
e_countries = list(filter(starts_with_e, countries))
print(e_countries)

print(".....................................(Q.6).............................")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even_numbers = list(
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
    )
print(squared_even_numbers)

print(".....................................(Q.6).............................")
def get_string_lists(lst):
    return list(filter(lambda x: type(x) == str, lst))
mixed_list = ['apple', 123, 'banana', 456, 'cherry', 789]
string_list = get_string_lists(mixed_list)
print(string_list)

print(".....................................(Q.6).............................")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

print(".....................................(Q.6).............................")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
concatenated_countries = reduce(lambda x, y: x + ', ' + y, countries)
sentence = concatenated_countries + " are north European countries"
print(sentence)

print(".....................................(Q.6).............................")
def categorize_countries(countries, starts_with):
    return [country for country in countries if country.startswith(starts_with)]
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
countries_starting_with_A = categorize_countries(countries, "A")
print(countries_starting_with_A)

print(".....................................(Q.6).............................")
def country_letter_count(countries):
    letter_count = {}
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    return letter_count
letter_count = country_letter_count(countries)
print(letter_count)

print(".....................................(Q.6).............................")
def get_first_ten_countries(countries):
    return countries[:10]


print(".....................................(Q.6).............................")




print(".....................................(Q.6).............................")
