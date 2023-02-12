
import random
import os
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear():
    return os.system('cls||clear')

def generate_number():
    number = random.randint(1,100)
    return number

def check_number(guess_number, answer, turns):
    '''Check answer and returns the number of turns'''
    if guess_number > answer:
        print("Too High")
        return turns -1
    elif guess_number < answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")
    
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def game():
    clear()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_result = generate_number()
    print(number_result)
    turns = set_difficulty()
    guess = 0
    while guess != number_result:        
        print(f"You have {turns} attempts left")
        guess = int(input("Make a guess: "))
        turns = check_number(guess_number=guess, answer=number_result, turns=turns)
        if turns == 0:
            print("You run out of turns, Game Over")
            return
        elif guess != number_result:
            print("Guess again")
    
game()