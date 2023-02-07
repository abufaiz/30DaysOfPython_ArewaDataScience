#Day 12: 30 Days of python programming
print("...................Exercise Level 1 (Q.1).............................")

import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print(random_user_id())

print(".................................(Q.2)................................")

def user_id_gen_by_user():
    length = int(input("Enter the number of characters for the ID: "))
    count = int(input("Enter the number of IDs to generate: "))
    chars = string.ascii_letters + string.digits
    user_ids = []
    for i in range(count):
        user_ids.append(''.join(random.choices(chars, k=length)))
    return user_ids

print(user_id_gen_by_user())
print(user_id_gen_by_user())

print(".................................(Q.3)................................")
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return "rgb({}, {}, {})".format(red, green, blue)
print(rgb_color_gen())

print(".................................(Q.4)................................")
def list_of_hexa_colors(n):
    hexa_colors = []
    for i in range(n):
        color = "#"
        for j in range(6):
            color += random.choice(string.hexdigits)
        hexa_colors.append(color)
    return hexa_colors
print(list_of_hexa_colors(5))

print("...................Exercise Level 2 (Q.1).............................")

def list_of_rgb_colors(num):
    rgb_colors = []
    for i in range(num):
        red = str(random.randint(0, 255))
        green = str(random.randint(0, 255))
        blue = str(random.randint(0, 255))
        rgb_colors.append("rgb(" + red + "," + green + "," + blue + ")")
    return rgb_colors
print(list_of_rgb_colors(5))

print(".................................(Q.2)................................")
def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return [''.join([random.choice('0123456789abcdef') for j in range(6)]) for i in range(num_colors)]
    elif color_type == 'rgb':
        return ['rgb({}, {}, {})'.format(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(num_colors)]
    else:
        return None
print(generate_colors(5, 7))

print(".................................(Q.3)................................")
def generate_colors(color_type, num):
    colors = []
    if color_type == 'hexa':
        for i in range(num):
            color = "#"
            for j in range(6):
                color += random.choice("0123456789abcdef")
            colors.append(color)
    elif color_type == 'rgb':
        for i in range(num):
            color = "rgb("
            for j in range(3):
                color += str(random.randint(0, 255))
                if j < 2:
                    color += ","
            color += ")"
            colors.append(color)
    return colors
print(generate_colors('hexa', 3)) 
print(generate_colors('hexa', 1)) 
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))  

print("...................Exercise Level 3 (Q.1).............................")
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(".................................(Q.2)................................")

def unique_random_numbers():
    random_numbers = random.sample(range(10), 7)
    return random_numbers

print(unique_random_numbers())
