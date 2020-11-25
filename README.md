# rock-papers-scissors-with-python

import random

name = str(input("Enter your name:\n"))

choices = ["rock", "papers", "scissors"]

print(f"Hi {name}, choose between rock, papers and scissors")

while True:
    user_choice = str(input('> '))
    user_choice = user_choice.lower()

    if user_choice not in choices:
        print(f"You chose {user_choice}, please choose rock, paper, or scissors")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")

    if user_choice == "rock":
        if computer_choice == "papers":
            print("Computer wins!")
        elif computer_choice == "scissors":
            print(f"{name} wins!")

    if user_choice == "papers":
        if computer_choice == "scissors":
            print("Computer wins!")
        if computer_choice == "rock":
            print(f"{name} wins!")

    if user_choice == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
        elif computer_choice == "papers":
            print(f"{name} wins!")

    if user_choice == computer_choice:
        print("Tie!")
