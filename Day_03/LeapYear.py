# Solução 1
# Leap Year / Ano Bissexto
print("Leap year / Ano Bissexto")
year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year!")
if year % 4 != 0 and year % 400 == 0:
    print("Leap year!")
if year % 4 != 0 and year % 400 != 0:
    print("NOT a Leap year!")

# Solução 2
# Leap Year / Ano Bissexto
print("Leap year / Ano Bissexto")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
