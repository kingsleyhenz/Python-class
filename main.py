# for a in range(5):
#     for b in range(3):
#         print(f"({a},{b})")


# for letter in "Kingsley":
#     print(f"{letter} is a letter")


# for no in [1,2,3,4,5,6]:
#     print(f"{no}")

# WHILE LOOP
# amount = 200
# while amount > 0:
#     print(f"{amount}")
#     amount //= 2

# option = "no"
 
# while option.lower() != "no":
#     option = input(">")
#     print("PRINT",option) 
    
# print("Bye Bye  ")    


# Infinite loop   
# while True:
#     option = input(">")
#     print("PRINT",option)
#     if option.lower() == "no":
#         break   


# count = 0
# for number in range(1,10):
#     if number % 2 == 0:
#         count += 1
# print(f"the number of even is :{count}")


# function

# def message(name):
#     # print(f"Hello {name}")
#     return f"Hello {name}"

# result = message("Beans")
# print(result)


# xargs
# def sum_of(*numbers):
#     sum = 0
#     for num in numbers:
#         sum += num
# print(sum)

# sum_of(1,2,3,4,5,6)


# xxargs
# def profile(**details):
#     print(details)
    
# profile(id="1", firstname="John", lastname="Doe",gender="Female",age=19)


# default

# def user_signup(fname, lname, status="Inactive"):
#     return fname + " " + lname + " " + status
# fname = input(" => Enter your firstname => ")
# lname = input(" => Enter your lastname => ")
# print(user_signup(fname,lname,"active"))

# list

letters = ["a", "b", "c", "d", "e", "f"]
# print(letters[0])
# zero = [0] * 50
# print(zero)
# add = zero + letters

num = list(range(31))
# print(num)

characters = list("King Henz")
# print(len(characters))  

#last
# print(letters[-1])

# last two
# print(letters[1:3])


mylen = len(letters)
# print(mylen)
# print(letters[:mylen])

#reverse 
# print(letters[::-1])

#list unpacking
prices = [20,30,50,90,1000,45,2345]
first,second,*third = prices
# print(f"first={first}, second={second}, third={third}")

# for index,chara in enumerate(letters):
    # print(index, chara)
    
# letters.append("f")
# print(letters)
# letters.insert(2,"Naomi")
# print(letters)

#remove
# letters.pop(2)
# print(letters)

#remove if index is now
# letters.remove("b")
# print(letters)

#delete
# del letters[1:3]
# print(letters)

#clear
# letters.clear()
# print(letters)

# print(letters.index("a"))

#sorting reverse order
# letters.sort(reverse=False)
# letters.sort(reverse=True)
# print(letters)

#tuples
people = [
    ("John", 30 , "male"),
    ("Mary", 23, "female"),
    ("Dan", 25, "male"),
    ("Zee", 33, "female")
]
people.sort()
print(people)
people.sort(key = lambda x : x[2])
