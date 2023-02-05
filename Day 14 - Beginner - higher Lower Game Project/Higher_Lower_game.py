import random
import os
from art import logo,vs
from Game_data import data

def clear():
    return os.system('cls||clear')

def Higher_Lower(option):
    if option == 'A' and optionA.get('follower_count') > optionB.get('follower_count'):
        print("You are right")
    else:
        print("you are wrong")

clear()

print(logo)
optionA = random.choice(data)
optionB = random.choice(data)

print(f"Compare A: {optionA.get('name')}, a {optionA.get('description')}, from {optionA.get('country')}")
print(vs)
print(f"Against B: {optionB.get('name')}, a {optionB.get('description')}, from {optionB.get('country')}\n")
option = input("Who has more followers? Type 'A' or 'B':").capitalize()
print(option)
Higher_Lower(option)
# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.