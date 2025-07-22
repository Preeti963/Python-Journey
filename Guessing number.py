import random

secret = random.randint(1,10)
guess = 0

while guess != secret:
    guess = int(input("Guess the number (between 1 to 10): "))

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Correct! you guessed it.")