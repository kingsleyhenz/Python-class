# MODULE
import random
import string
# 1. Write a function that generates a six-digit/character random_user_id.
def random_user_id():
    chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return chars
# print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs that are supposed to be generated.
def user_id_gen_by_user():
    chars_num = int(input("Enter the number of characters per ID: "))
    Id_num = int(input("Enter the number of IDs to generate: "))
    chars = string.ascii_letters + string.digits
    users_Id = ''
    count = 0
    random_chars = []
    iter_num = Id_num * chars_num
    for i in range(iter_num):
        count += 1
        random_num = random.randrange(0, len(chars))
        users_Id += chars[random_num]
        if count == chars_num:
            random_chars.append(users_Id)
            count = 0
            users_Id = ''
    return random_chars
# ids = user_id_gen_by_user()
# for id in ids:
#     print(id)

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
# print(rgb_color_gen())

# 3a. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
def list_of_hexa_colors(hex_color_num):
    letters = string.ascii_letters.lower()[0:6] + string.digits
    gen_colors = []
    hexa_chars = ''
    for _ in range(6 * hex_color_num):
        random_num = random.randrange(0, len(letters))
        hexa_chars += letters[random_num]

        if len(hexa_chars) == 6:
            gen_colors.append("#{}".format(hexa_chars))
            hexa = ''
    return gen_colors
hex_colors = list_of_hexa_colors(1)
# print(hex_colors)

# 3b. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_colors(num_colors):
    colors = []
    for i in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"rgb({r}, {g}, {b})"
        colors.append(color)
    return colors
rgb_colors = list_of_colors(3)
# print(rgb_colors)

# 3c. 
def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_colors(num_colors)
    else:
        return []
rgb_colors = generate_colors('rgb', 3)
# print(rgb_colors)


# 4. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffled_lst = lst[:]
    random.shuffle(shuffled_lst)
    return shuffled_lst
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
# print(shuffled_list)

# 5. Write a function that returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def generate_unique_numbers():
    numbers = random.sample(range(10), 7)
    return numbers
random_numbers = generate_unique_numbers()
# print(random_numbers)
