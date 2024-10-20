'''Blackjack Capstone Project'''

import random

LOGO = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

PLAYER_WINS = 0
CPU_WINS = 0


# Build an actual card system instead of just pulling random numbers.
# This will require the game to become round based on the size of a deck.

def deal_card():
    """Returns a random card from a deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score(cards):
    """Compares the user score against the CPU"""
    # Handles the Blackjack condition.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Changes ace from 10 to 1 instead.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def hand_calculation(user_score, cpu_score):
    """Compares the users score to the CPU to determine the winning hand"""
    if user_score == cpu_score:
        return "Draw!"
    elif cpu_score == 0:
        return "Loss, the CPU has a Blacjack!"
    elif user_score == 0:
        return "Win! You have a blackjack."
    elif user_score > 21:
        return "You've went over 21, you lose."
    elif cpu_score > 21:
        return "The house has bust, you win!"
    elif user_score > cpu_score:
        return "You win!"
    else:
        return "You lose."

def game():
    """Main gameplay loop."""
    gameover = False
    user_cards = []
    cpu_cards = []
    user_score = -1
    cpu_score = -1

# The underscore disregards the need to track that variable, only needing the range.
    for _ in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while not gameover:
        user_score = score(user_cards)
        cpu_score = score(cpu_cards)
        
        # Add a money and betting system.
        # player_money = 2500

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            gameover = True
        else:
            user_should_deal = input("Type 'y' to hit, type 'n' to stand:\n> ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                gameover = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = score(cpu_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(hand_calculation(user_score, cpu_score))

def main():
    """Main Program Loop"""
    print(LOGO)
    running = True
    while running:
        choice = input("Welcome to Blackjack, would you like to play a game?\n> ").lower()
        if choice == "yes":
            print("\n" * 20)
            game()
        elif choice == "no":
            running = False
            exit()

main()
# Create proper main menu.
