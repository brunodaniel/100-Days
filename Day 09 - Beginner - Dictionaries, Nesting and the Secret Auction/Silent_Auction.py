import os
choice = True
bid = {}
winner_bid = 0
winner_name = ""

def add_new_bid(name, price):
    bid[name] = price

while choice:
    name = input("Enter yout name: ")
    price = int(input("Enter your bid: $"))
    add_new_bid(name=name, price=price)
    other_bids = input("Any other bids? Yes or No\n").lower()
    if other_bids == "yes":
        os.system('cls||clear')
    else:
        choice = False
        
for key in bid:
    if bid[key] > winner_bid:
        winner_bid = bid[key]
        winner_name = key
        
print(f"The winner is {winner_name} with a bid of ${winner_bid}")
