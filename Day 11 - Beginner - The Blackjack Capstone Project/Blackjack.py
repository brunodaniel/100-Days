import os
import random
from art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player = 0
dealer = 0
player_hand = []
dealer_hand = []

def clear():
    return os.system('cls||clear')
# def check_hands(player_hand, dealer_hand):
#     if player_hand == 21 and dealer_hand < 21:
#         return True
#     elif player_hand < dealer_hand:
#         return False
    
def draw_card():
    return cards[random.randint(0, len(cards))]

def first_draw():
    player_hand.append(draw_card())
    player_hand.append(draw_card())
    dealer_hand.append(draw_card())
    player = sum(player_hand)
    

def blackjack():    
    
    should_continue = True   
    while should_continue:
        clear()
        print(logo)   
        
        print(player_hand)
        if input("New game?: 'y' or 'n'").lower() == 'y':
            print("again")
        else:
            print("bye")
            should_continue = False
            #blackjack()
            
blackjack()