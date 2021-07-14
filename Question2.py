# Part a) 
# Ask the user for their name, age, email and add their details to a list.
# Part b)
# If their age is greater than 18 AND their name starts with the letter “S”, tell them that they are allowed entry to the game.
# Otherwise, if their email is longer than 15 letters (including ‘@gmail.com’), they are allowed entry to the game.
# If both the above conditions don’t match, they can’t play the game (print this out).


name = input("What is your name? ")
age = int(input("What is your age? "))
email = input("What is your email? ")

user_details = [name, age, email]


if (age > 18 and name[0] == 'S') or len(email) > 15:
    print("You can play")
else:
    print("You can't play")
