print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
LorR = input(
    "You're at a cross road. Where do want to go? Type 'left' or 'right'\n").lower()
if(LorR == 'left'):
    WorS = input("You come to a lake. there is a island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if(WorS == 'wait'):
        doors = input(
            "You arrive on teh island unharmed. There is a house with 3 doors. One red, one Yellow and one Blue. Which color do you choose?\n").lower()
        if(doors == "yellow"):
            print("You Win!!!")
        elif(doors == "blue"):
            print("Eaten by beasts. GAME OVER.")
        elif(doors == "red"):
            print("Burned by fire. GAME OVER.")
        else:
            print("GAME OVER.")
    else:
        print("Attacked by trout. GAME OVER.")
else:
    print("Fall into a hole. GAME OVER.")
