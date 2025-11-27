import random

def play_game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")

    # Choose difficulty
    print("\nChoose difficulty:")
    print("1. Easy (Unlimited tries)")
    print("2. Hard (Only 5 tries)")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        attempts_allowed = None  # Unlimited
    elif choice == "2":
        attempts_allowed = 5
    else:
        print("Invalid choice! Defaulting to Easy mode.")
        attempts_allowed = None

    # Generate random number
    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        # Compare guess
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"\n🎉 Correct! You guessed the number in {attempts} attempts.")
            break

        # If Hard mode & attempts exceeded
        if attempts_allowed is not None and attempts >= attempts_allowed:
            print("\n❌ You're out of attempts!")
            print(f"The correct number was {secret_number}.")
            break


# Main program loop (Replay option)
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\nThanks for playing! 👋")
        break
