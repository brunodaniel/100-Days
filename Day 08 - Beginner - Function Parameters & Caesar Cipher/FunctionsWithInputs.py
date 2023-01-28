def greet_with_name(name):
    print(f"Hello {name}")


greet_with_name("Bruno")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")


greet_with("Bruno", "São Paulo")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")


name = input("Enter your name: ")
location = input("Enter your location: ")

greet_with(location=location, name=name)
