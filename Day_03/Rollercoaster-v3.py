# Rollercoaster 3.0
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("The price is $5")
    elif age <= 18:
        bill = 7
        print("The price is $7")
    elif age >= 45 and age <= 55:
        print("The ride is free")
    else:
        bill = 12
        print("The price is $12")

    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y":
        bill += 3
    print(f"The final bill is ${bill}")
else:
    print("You can not ride the rollercoaster")
