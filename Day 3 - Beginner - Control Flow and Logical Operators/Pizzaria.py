# Pizzaria
print("----------------------\nSmall Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\nPepperoni for Small \nPizza: +$2\nPepperoni for Medium or Large Pizza: +$3\nExtra cheese for any size pizza: + $1\n-------------------------")
size = input("Chose teh pizza size: S for Small, M for Medium and L for Large ")
add_peperoni = input("Extra Peperoni? Y or N ")
add_cheese = input("Extra Cheese? Y or N ")
bill = 0
if size == 'S':
    bill = 15
    if add_peperoni == 'Y':
        bill = bill + 2
        if add_cheese == 'Y':
            bill = bill + 1
if size == 'M':
    bill = 20
    if add_peperoni == 'Y':
        bill += 3
        if add_cheese == 'Y':
            bill += 1
if size == 'L':
    bill = 25
    if add_peperoni == 'Y':
        bill += 3
        if add_cheese == 'Y':
            bill += 1
print(bill)
print(f"Total Bill: ${bill}")
