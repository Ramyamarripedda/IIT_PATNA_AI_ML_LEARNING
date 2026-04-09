# 1)Take a number as input and print its square
#---------------------------------------------------------------
# number = int(input("enter a number:"))
# print(f"the square of {number} is {number * number}")

# 2)Take two numbers and print their sum, difference, multiplication
#-----------------------------------------------------------------
# number1 = int(input("enter your number:"))
# number2 = int(input("enter your number:"))
# print(f" sum of {number1} + {number2} = {number1 + number2}")
# print(f" sub of {number1} - {number2} = {number1 - number2}")
# print(f" mul of {number1} x {number2} = {number1 * number2}")

# 3)Take your name and age and print:
# My name is ___ and I am ___ years old
#------------------------------------------------------------------
# name = input("enter your name: ")
# age = int(input("enter your age:"))
# print(f"My name is {name} and I am {age} years old")

# 4)Convert a string "50" into integer and add 10
#--------------------------------------------------------------
# number = "50"
# print(int(number) + 10)

# 5)Take a float input and convert it into integer
#--------------------------------------------------------------
# number = 72.56
# print(int(number))

# 6)Take two numbers and check: which one is greater in this question i need to ask input ?
#----------------------------------------------------------------------------------------
# number1 = int(input("enter your number:"))
# number2 = int(input("enter your number:"))
# if number1 > number2:
#     print(f"{number1} is grater than {number2}")
# elif number2 > number1:
#     print(f"{number2} is grater than {number1}")
# else:
#     print(f"{number1} and {number2} both are equal")

# 7)Check if a number is even or odd
#--------------------------------------------------------------
# number = int(input("enter a number:"))
# if number % 2 ==0:
#     print(f"{number} is a even number")
# else:
#     print(f"{number} is a odd number")

# 8)Take a number and check:
# is it greater than 100? 
#--------------------------------------------------------
target = 100
number = int(input("enter a number:"))
if number > target:
    print(f"{number} is grater than {target}")
elif number < target:
    print(f"{number} is less than {target}")
else:
    print(f"{number} and {target} both are equal")


