# BMI Calculator 2.0
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = round(weight / height ** 2)
print("Your BMI is: " + str(bmi))
if bmi < 18.5:
    print("You are UNDERWEIGHT")
elif bmi < 25:
    print("You have NORMAL WEIGHT")
elif bmi < 30:
    print("You have OVERWEIGHT")
elif bmi < 35:
    print("You have OBESE")
elif bmi > 35:
    print("You have CLINICALLY OBESE")
