import random

response = "y"

while response == "y":
    num = random.randint(1,6)
    print(f"You rolled a {num}!")
    response = input("Do you want to roll again (enter y or n)? ")

    if response == "n":
        print("Ok, goodbye.")
        break