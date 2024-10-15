'''Day 7 Big Project, making a hangman game.'''

import random
from hangman_words import WORD_LIST
from hangman_art import STAGES, LOGO

CORRECT_LETTERS = []

LIVES = 6

print(LOGO)

PLACEHOLDER = ""
CHOSEN_WORD = random.choice(WORD_LIST)
GAME_OVER = False
print("Debug Answer:" + CHOSEN_WORD)

WORD_LENGTH = len(CHOSEN_WORD) # int(CHOSEN_WORD.count("")) - 1
for position in range(WORD_LENGTH):
    PLACEHOLDER += "_"
print(PLACEHOLDER)


while not GAME_OVER: # While loop that checks if game is active.
    print(f"*****{LIVES}/6 LIVES LEFT*****")
    GUESS = input("Guess a LETTER: ").lower()
    # print(GUESS)

    if  GUESS in CORRECT_LETTERS:
        print(f"You've already guessed {GUESS}.")

    DISPLAY = ""
    for LETTER in CHOSEN_WORD:
        if LETTER == GUESS:
            DISPLAY += LETTER
            CORRECT_LETTERS.append(GUESS)
        elif LETTER in CORRECT_LETTERS:
            DISPLAY += LETTER
        else:
            DISPLAY += "_"

    print("Current Word: " +DISPLAY)

    if GUESS not in CHOSEN_WORD:
        LIVES -= 1
        print(f"You guessed {GUESS}, that's not in the word. You lose a life.")
        if LIVES == 0:
            GAME_OVER = True
            print(f"The correct word was {CHOSEN_WORD}.")
            print("*****You Lose.*****")

    if "_" not in DISPLAY:
        GAME_OVER = True
        print("*****You win!*****")

    print(STAGES[LIVES]) # Since HP starts at six, it will print the list of ASCII art backwards.
