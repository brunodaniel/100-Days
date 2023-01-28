# Rollercoaster 1.0
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("The price is $5")
    elif age <= 18:
        print("The price is $7")
    else:
        print("The price is $12")
else:
    print("You can not ride the rollercoaster")
