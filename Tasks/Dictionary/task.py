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
print(skill_count)
print(type(skill_count))
