'''Creating the "High or Low" game from FFXIV Shadowbringers.'''
# Inspired by https://ffxiv.pf-n.co/high-or-low

import sys
import random

LOGO = r"""
  ___ ___ .__       .__                     .____                  
 /   |   \|__| ____ |  |__     ___________  |    |    ______  _  __
/    ~    \  |/ ___\|  |  \   /  _ \_  __ \ |    |   /  _ \ \/ \/ /
\    Y    /  / /_/  >   Y  \ (  <_> )  | \/ |    |__(  <_> )     / 
 \___|_  /|__\___  /|___|  /  \____/|__|    |_______ \____/ \/\_/  
       \/   /_____/      \/                         \/             
"""

def score_calculation(guess, cpu_sum, user_sum):
    """Calculates win condition based on user guess."""
    if cpu_sum > user_sum and guess == "low":
        print("Correct!")
        return True
    elif user_sum > cpu_sum and guess == "high":
        print("Correct")
        return True
    else:
        print("Incorrect!")
        return False

def game():
    """Main Game Loop."""
    gameover = False
    while not gameover:
        user_cards = []
        cpu_cards = []
        deck = list(range(1, 10))
        user_cards = random.sample(deck, 3)
        remaining_cards = [n for n in deck if n not in user_cards]
        cpu_cards = random.sample(remaining_cards, 3)
        user_sum = sum(user_cards)
        cpu_sum = sum(cpu_cards)
        current_round = 1
        print(f"Welcome to Round {current_round}.")
        print(f"Your cards are {user_cards[0]}")
        print(f"Tista-Bie's cards are {cpu_cards[0]} and {cpu_cards[1]}")
        print("You must guess if the sum of your three cards is higher or lower than the sum of her three cards.")
        guess = input("So what will it be, high or low?\n> ")
        answer = score_calculation(guess, cpu_sum, user_sum)
        if answer is True:
            print("Would you like to play again?\n> ")
            break
        else:
            print("You lose.")
            gameover = True

def main():
    """Main Program Loop"""
    print(LOGO)
    running = True
    while running:
        choice = input("Welcome to the beehive, would you like to play a game?\n> ").lower()
        if choice == "yes":
            print("\n" * 10)
            game()
        elif choice == "no":
            running = False
            exit()

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit(0)
