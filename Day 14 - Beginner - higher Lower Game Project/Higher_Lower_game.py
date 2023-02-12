
import random
import os
from art import logo,vs
from game_data import data
score = 0
game_over = True
def clear():
    return os.system('cls||clear')

def Higher_Lower(option):
    '''Check if user is correct.'''
    if option == 'A' and optionA.get('follower_count') > optionB.get('follower_count'):
        return "A"
    else:
        return "B"

clear()

def Random_option():
    return random.choice(data)


# Generate a random account from the game data.
optionA = Random_option()
optionB = Random_option()

def jogo():
    score = 0
    game_over = True
    optionA = Random_option()
    optionB = Random_option()
    while game_over:
        print(logo)
        if optionA.get('name') == optionB.get('name'):
            optionB
        # Format account data into printable format.
        print(f" Your score is: {score}")
        print(f"Compare A: {optionA.get('name')}, a {optionA.get('description')}, from {optionA.get('country')}")
        print(vs)
        print(f"Against B: {optionB.get('name')}, a {optionB.get('description')}, from {optionB.get('country')}\n")
        # Ask user for a guess.
        option = input("Who has more followers? Type 'A' or 'B':").capitalize()
        # Check if user is correct.
        result = Higher_Lower(option)


        if result == 'A':
            if option == result:
                score += 1
                optionB = Random_option()
                clear()
            else:
                print("Wrong choice")
        elif result == 'B':
            if option == result:
                score += 1
                optionA = optionB
                optionB = Random_option()
                clear()
            else:
                print("Wrong choice")
                print(f"You score is: {score}")
                game_over = False



jogo()





## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.