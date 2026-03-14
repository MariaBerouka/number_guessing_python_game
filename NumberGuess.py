import random

# 1. We define the game here
def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Spot on! You found it in {attempts} attempts.")
                break
        except ValueError:
            print("That's not a number! Please enter a whole number.")

# 2. THIS IS THE KEY: We must tell the computer to actually RUN the game.
# Make sure this line has NO spaces before it.
start_game()