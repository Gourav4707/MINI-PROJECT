import random

choices = ["stone", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        return "User"
    else:
        return "Computer"

def play_game():
    user_score = 0
    comp_score = 0

    while True:
        print("\n1. Play Round")
        print("0. Exit Game")
        choice = input("Enter choice: ")

        if choice == "1":
            user = input("Enter stone/paper/scissors: ").lower()
            if user not in choices:
                print("Invalid choice!")
                continue

            computer = get_computer_choice()
            print(f"Computer chose: {computer}")

            winner = decide_winner(user, computer)

            if winner == "User":
                print("You win!")
                user_score += 1
            elif winner == "Computer":
                print("Computer wins!")
                comp_score += 1
            else:
                print("It's a draw!")

            print(f"Score -> You: {user_score}, Computer: {comp_score}")

        elif choice == "0":
            break
        else:
            print("Invalid choice!")