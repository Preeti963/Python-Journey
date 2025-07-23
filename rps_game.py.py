import random

choices = ["rock", "scissors", "paper"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    elif user_choice not in choices:
        print("Invalid input! Please choose rock, paper, or scissors.")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
