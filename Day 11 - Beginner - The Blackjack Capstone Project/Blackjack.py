import os
import random
from art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_score = 0
dealer_score = 0
player_hand = []
dealer_hand = []

def clear():
    return os.system('cls||clear')

    
def draw_card():
    return cards[random.randint(0, len(cards))]

def first_draw():
    player_hand.append(draw_card())
    player_hand.append(draw_card())
    dealer_hand.append(draw_card())
    


def blackjack():    
    
    should_continue = True   
    while should_continue:
        clear()
        print(logo)   
        first_draw()
        player_score = sum(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer first card: {dealer_hand}")
        if input("New game?: 'y' or 'n'").lower() == 'y':
            print("again")
        else:
            print("bye")
            should_continue = False
            
            
blackjack()