while True:
    user_input = input("Enter a number (or type 'exit' to quit): ").lower()

    if user_input == 'exit':
        print("Thanks for using the Even/Odd Checker")
        break

    if not user_input.isdigit():
        print("Invalid input! please enter a valid number.")
        continue

    number = int(user_input)

    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")