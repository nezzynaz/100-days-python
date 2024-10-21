'''Number Guessing Game Project'''

import sys
from random import randint

LOGO = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
EASY_DIFFICULTY = 15
HARD_DIFFICULTY = 5

# Function to check users' guess against actual answer
def checkanswer(user_guess, answer, turns):
    """Compares the user's guess to the answer."""
    if user_guess > answer:
        print("Too High")
        return turns - 1
    elif user_guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"Correct answer! The answer was {answer}")
        return

# Function to set difficulty
def difficulty():
    """Sets difficulty to either easy or hard."""
    level = input("Choose a difficulty, easy or hard?\n> ").lower()
    if level == "easy":
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY

# Function for Game itself
def main():
    """Main Game Function."""
    print(LOGO)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 20.")
    answer = randint(1, 20)
    turns = difficulty()
    print(f"DEBUG: Answer is {answer}!")

    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left to guess the number.")
        guess = int(input("Make a guess.\n> "))
        turns = checkanswer(guess, answer, turns)
        if turns == 0:
            print("You've ran out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again!")

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit(0)
