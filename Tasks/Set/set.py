# SET LEVEL 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# 1. Find the length of the set it_companies
length_it_companies = len(it_companies)
# print(length_it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
# print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Netflix', 'Spotify'])
# print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Microsoft')
print(it_companies)

# 5. What is the difference between remove and discard
# The remove() method raises a KeyError if the element does not exist in the set, whereas the discard() method does nothing if the element does not exist.

# SET LEVEL 2
# 1. Join A and B
union_AB = A.union(B)
# print(union_AB)

# 2. Find A intersection B
intersection_AB = A.intersection(B)
# print(intersection_AB)

# 3. Is A subset of B
is_A_subset_of_B = A.issubset(B)
# print(is_A_subset_of_B)

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
# print(are_disjoint)

# 5. Join A with B and B with A
join_AB = A.union(B)
join_BA = B.union(A)
# print(join_AB)
# print(join_BA)

# 6. What is the symmetric difference between A and B
symm_diff_AB = A.symmetric_difference(B)
print(symm_diff_AB)

# 7. Delete the sets completely
del it_companies
del A
del B

#  SET LEVEL 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
length_age_list = len(age)
length_age_set = len(ages_set)
# print(ages_set)
# print(length_age_list)
# print(length_age_set)

# 2. Explain the difference between the following data types: string, list, tuple and set
# - String: A sequence of characters. It is immutable, meaning it cannot be changed once created.
# - List: An ordered collection of items. It is mutable, meaning it can be modified.
# - Tuple: An ordered collection of items. It is immutable, meaning it cannot be changed once created.
# - Set: An unordered collection of unique items. It does not allow duplicate values.

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
num_unique_words = len(unique_words)
print("Number of unique words in the sentence:", num_unique_words)
