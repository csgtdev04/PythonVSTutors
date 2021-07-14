# Write the code to print out if an inputted number is even or odd.

# steps:
# ask the user to input an integer


# method 1
num = int(input("Enter a number: ")) 

# an even number does not have a remainder when divided by 2

mod = num % 2
if mod > 0:
    print("This is an odd number. ")
else: 
    print("This is an even number. ")



# method 2
userNumber = int(input("Please Enter An Integer : "))
if userNumber % 2 == 0:
  print("This number is Even")
else:
  print("This number is Odd")







