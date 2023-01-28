import math
def prime_checker(number):
    if ((math.factorial(number-1)+1)%number):
        print("The number is not prime")
    else:
        print("The number is prime")

n = int(input("Check this number: "))
prime_checker(number=n)