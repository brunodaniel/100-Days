print("Welcome to the tip calculator.")
totalbill = float(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give? 10,12 or 15 "))
qtdpeople = int(input("How many people to split the bill into? "))
percentage = float(perc/100)+1
round_total = ((totalbill/qtdpeople)*percentage)
round_total = "{:.2f}".format(round_total)
print(f"Each person should pay: ${round_total}")
