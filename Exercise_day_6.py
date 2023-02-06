#Day 6: 30 Days of python programming

print("...........................Exercise Level 1 (Q. 1)............................")
tpl = ()
print ('Empty Tuple :', tpl)

print("............................................(Q. 2)............................")
male_siblings = ('Hussaini', 'Sani', 'Gambo', 'Auwalu')
female_siblings = ('Sadiya', 'Zainab', 'Maryam')
print(male_siblings)
print(female_siblings)

print("............................................(Q. 3)............................")
siblings = male_siblings + female_siblings
print("My Siblings are:", siblings) 

print("............................................(Q. 4)............................")
no_of_siblings = len(siblings)
print(no_of_siblings)

print("............................................(Q. 5)............................")
father_name = "Adamu"
mother_name = "Habiba"
family_members = siblings + (father_name, mother_name)
print(family_members)


print("...........................Exercise Level 1 (Q. 2)............................")

print("............................................(Q. 1)............................")
siblings, parents = family_members[:7], family_members[7:]
print("Siblings:", siblings)
print("Parents:", parents)

print("............................................(Q. 2)............................")
fruits = ('apple', 'banana', 'peach')
vegetables = ('carrot', 'lettuce', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

print("............................................(Q. 3)............................")
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)


print("............................................(Q. 4)............................")
food_stuff_tp = fruits + vegetables + animal_products
middle_items_tp = food_stuff_tp[len(food_stuff_tp)//2-1:len(food_stuff_tp)//2+2]
print(middle_items_tp)

print("............................................(Q. 5)............................")
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

print("............................................(Q. 6)............................")
food_stuff_tp = fruits + vegetables + animal_products
del food_stuff_tp

print("............................................(Q. 7)............................")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print("Estonia is a nordic country.")
else:
    print("Estonia is not a nordic country.")

if 'Iceland' in nordic_countries:
    print("Iceland is a nordic country.")
else:
    print("Iceland is not a nordic country.")
