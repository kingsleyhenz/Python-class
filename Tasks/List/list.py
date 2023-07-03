# LIST LEVEL 1

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
my_list = [10, 21, 'Jedi', 'Bro', True, 'Done']
# print(my_list)

# 3. Find the length of your list
list_length = len(my_list)
# print(list_length)

# 4. Get the first item, the middle item and the last item of the list
first_item = my_list[0]
middle_item = my_list[len(my_list)//2]
last_item = my_list[-1]
# print(first_item) 
# print(middle_item)
# print(last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Henz', 10, 10.75, 'Married', '123 Woji Street']
# print (mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
num_companies = len(it_companies)
# print("companies count:", num_companies)

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]
# print("First:", first_company)
# print("Middle:", middle_company)
# print("Last:", last_company)

# 10. Print the list after modifying one of the companies
it_companies[2] = 'Chevron Limited'
# print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Intel')
# print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Oracle')
# print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[it_companies.index('IBM')] = it_companies[it_companies.index('IBM')].upper()
# print(it_companies)

# 14. Join the it_companies with a string '#;  '
joined_companies = '#; '.join(it_companies)
# print("Joined companies:", joined_companies)

# 15. Check if a certain company exists in the it_companies list.
company_exists = 'Apple' in it_companies
# print("Does Apple exist in the list?", company_exists)

# 16. Sort the list using sort() method
it_companies.sort()
# print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
# print(it_companies)

# 18. Slice out the first 3 companies from the list
first_3_companies = it_companies[:3]
# print(first_3_companies)

# 19. Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]
# print(last_3_companies)

# 20. Slice out the middle IT company or companies from the list
middle_companies = it_companies[len(it_companies)//2:(len(it_companies)//2)+1]
print(middle_companies)

# 21. Remove the first IT company from the list
del it_companies[0]


# 22. Remove the middle IT company or companies from the 
del it_companies[len(it_companies)//2]


# 23. Remove the last IT company from the list
del it_companies[-1]


# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
# print(joined_list)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()
full_stack.insert(joined_list.index('Redux')+1, 'Python')
full_stack.insert(joined_list.index('Redux')+2, 'SQL')
# print("Full stack:", full_stack)