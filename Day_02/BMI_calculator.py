# BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = int(weight/height**2)
print("Your BMI is: " + str(bmi))
