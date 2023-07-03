# DICTIONARY
# 1. CREATE AN EMPTY DICTIONARY CALLED DOG
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Fido', 'color': 'brown', 'breed': 'Labrador Retriever', 'legs': 4, 'age': 5}
# print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'King',
    'last_name': 'Henz',
    'gender': 'Male',
    'age': '34',
    'marital_status': 'Happily Married',
    'skills': ['Football', 'Tennis', 'BasketBall', 'NodeJs'],
    'country': 'Nigeria',
    'city': 'Port-Harcourt',
    'address': 'Woji'
}

# 4.Get the length of the student dictionary 
length = len(student)
# print(length)

# 5. Get the value of skills and check the data type, it should be a list
skill_count = student['skills']
# print(skill_count)
# print(type(skill_count))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('MongoDb')
student['skills'].append('ReactJs')
# print(student['skills'])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
# print(keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
# print(values_list)

# 9. Change the dictionary to a list of tuples using items() method
student_tuple = list(student.items())
# print(student_tuple)

# 10. Delete one of the items in the dictionary
del student['address']
print(student)