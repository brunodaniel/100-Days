import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_int = random.randint(0, len(names)-1)
person = names[random_int]
print(person + " will pay the bill")
