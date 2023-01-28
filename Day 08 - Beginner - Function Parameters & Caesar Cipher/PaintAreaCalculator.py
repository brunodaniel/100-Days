from math import ceil
def paintarea(height, width, coverage):
    number_of_can = ceil((height * width)/coverage)
    print(f"You will need {number_of_can} cans of paint")

coverage = 5
height = float(input("Enter the height of the wall: "))
width = float(input("Enter the width of the wall: "))
paintarea(height, width, coverage=coverage)