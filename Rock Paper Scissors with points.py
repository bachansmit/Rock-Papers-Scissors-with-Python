import random

name = str(input("Enter your name:\n"))

choices = ["rock", "papers", "scissors"]

print(f"Hi {name}, choose between rock, papers and scissors. You can also quit the game by writing quit.")

computer_wins = 0
user_wins = 0
tie = 0


def points_tally():
    print()
    print(f"Computer victories so far: {computer_wins}")
    print(f"User victories so far: {user_wins}")
    print(f"Ties so far: {tie}")
    print()


while True:
    user_choice = str(input('> '))
    user_choice.lower()

    if user_choice == "quit":
        print("FINAL SCORES:")
        print(f"User wins: {user_wins} times")
        print(f"Computer wins: {computer_wins} times")
        print(f"No. of ties: {tie}")
        break

    if user_choice not in choices:
        print("ERROR")

    else:
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

    if user_choice == "rock":
        if computer_choice == "papers":
            print("Computer wins!")
            computer_wins += 1
            points_tally()

        elif computer_choice == "scissors":
            print(f"{name} wins!")
            user_wins += 1
            points_tally()

    if user_choice == "papers":
        if computer_choice == "scissors":
            print("Computer wins!")
            computer_wins += 1
            points_tally()

        elif computer_choice == "rock":
            print(f"{name} wins!")
            user_wins += 1
            points_tally()

    if user_choice == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
            computer_wins += 1
            points_tally()

        elif computer_choice == "papers":
            print(f"{name} wins!")
            user_wins += 1
            points_tally()

    if user_choice == computer_choice:
        print("Tie!")
        tie += 1
        points_tally()
