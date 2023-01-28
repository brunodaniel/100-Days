import os
import random
from art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player = 0
dealer = 0
def clear():
    return os.system('cls||clear')
# def check_hands(player_hand, dealer_hand):
#     if player_hand == 21 and dealer_hand < 21:
#         return True
#     elif player_hand < dealer_hand:
#         return False
    
def draw_card():
    return cards[random.randint(0, len(cards))]

def blackjack():    
    
    should_continue = True   
    while should_continue:
        clear()
        print(logo)   
        
        
        if input("New game?: 'y' or 'n'").lower() == 'y':
            print("again")
        else:
            print("bye")
            should_continue = False
            #blackjack()
            
blackjack()