# Given a string and an integer number n,
# remove characters from a string starting from zero up to n and return a new string

# input
# logic
# output - print, return

user_string = input("Enter A String: ")
n = int(input("Enter a positive integer number: " ))

def removeChars(user_string, n):
    if n < 0:
      n2 = int(input("Enter a positive integer number: "))
      # print(user_string[n2+1:])
      return user_string[n2+1:]
    else:
      # print(user_string[n+1:])
      return user_string[n+1:]

output = removeChars()
print(output)

if output == "hi":
    print("the output is hi!")



# 1. ask the user for input
# 2. define the function, include the input parameters
# 3. logic part, where you actually answer the question
# 4. use either print or return
# 5. trigger the function (if u use return, you need to save it in a variable, otherwise write the name of the function())

# given the user's age, return if the user can vote.  

# 2. input
# 2. logic
# 1. return 
# 2. points for triggering the function and printing the output