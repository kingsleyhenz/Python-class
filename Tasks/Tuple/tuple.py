# TUPLE #LEVEL 1
# 1. Create an empty
my_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers
sisters = ('Sophia', 'Nana', 'Sophia')
brothers = ('Jedi', 'Henz', 'Swagga')
# print(sisters)
# print(brothers)
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
# print(siblings)
# 4. How many siblings do you have?
num_siblings = len(siblings)
# print(num_siblings)
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Ayo', 'Kate')
# print(family_members)



# LEVEL 2
# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'spinach', 'tomato')
animal_products = ('meat', 'milk', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
# print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items_tp = food_stuff_tp[len(food_stuff_tp)//2]
middle_items_lt = food_stuff_lt[len(food_stuff_lt)//2]
# print(middle_items_lt)
# print(middle_items_tp)

# 5. Slice out the first three items and the last three items from food_staff_lt list
sliced_items_lt = food_stuff_lt[:3] + food_stuff_lt[-3:]
# print(sliced_items_lt)

# 6. Delete the food_staff_tp tuple completely
# 7. Check if an item exists in tuple:
# 8. Check if 'Estonia' is a nordic country
# 9. Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

