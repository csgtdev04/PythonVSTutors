# What is a function
# a function is a block of code that has some purpose

# Why do we use functions
# modularize/organize code


# How many steps are there to use functions


# What are the parts of a function


def print_hello_world():
    print("Hello World")

print_hello_world()
print(23 * 16)
if 10 * 10 > 50:
    print("Hi")
print_hello_world()


current_year = 2021
user_dob = int(input("What year were you born in? "))
# print("You are currently", current_year - user_dob, "years old")

def calculate_user_age(current_year, user_dob):
   user_age = current_year - user_dob
   return user_age

user_age = calculate_user_age(current_year, user_dob)
print(user_age)


# function declaration
def calculator(first_number, operation, second_number):
    if operation == "+":
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == 'x':
        print(first_number * second_number)
    elif operation == '/':
        print(first_number / second_number)
    else:
        print("Our calculator doesn't support these features yet!")


result = calculator(7, "+", 8)
print(result)


   


# Given 2 numbers from the user (input), if their product is greater than 1000, RETURN (ouput) their sum, otherwise if the product is less than 1000, RETURN their product






    

