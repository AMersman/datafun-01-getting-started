"""
Optional bonus. See course site for details.
Ashley Mersman, gamebot using logic, 1/14/2023
"""

import random

# Change the name below to a name of your choice

name = "Nature's Choice"

# Fix the code below to print the name using an f-string

print()
print(f"Hello, I'm {name}, your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function

user_choice = input('Choose wolf, eagle, or snake.')

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
if user_choice == buddy_choice:
    print("We tied!")
if user_choice == "wolf":
    if buddy_choice == "eagle":
        print("You win! Wolf scares eagle.")
    elif buddy_choice == 'snake':
        print("You lose. Snake bites wolf.")
if user_choice == "eagle":
    if buddy_choice == "wolf":
        print("You lose! Wolf scares eagle.")
    elif buddy_choice == 'snake':
        print("You win. Eagle grabs snake.")
if user_choice == "snake":
    if buddy_choice == "wolf":
        print("You win! Snake bites wolf.")
    elif buddy_choice == 'eagle':
        print("You lose. Eagle grabs snake.")


# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""
You said wolf.
I said snake.

You lose. Snake bites wolf.
"""

"""Ashley Mersman, 1/14/2023, Game-bot"""
