'''Day 14 Assignment - Higher or Lower Game.'''

# Based heavily off the solution problem from the pycharm resource. I edited it to make it more
# fun and fixed weird logic that I didn't like.

import random
from assets import LOGO, VS, data

# Take account data and return it into printable format
def format_data(account):
    """Takes data from the dictionary and converts it to f strings"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"

# Take a user guess and compare follower counts
def check_answer(a_followers, b_followers):
    """Checks which follower count is higher."""
    if a_followers > b_followers:
        return "a"
    else:
        return "b"

GAME_OVER = False
SCORE = 0
HIGHSCORE = 0
LIVES = 5

print(LOGO)

while not GAME_OVER:
    print(f"Current SCORE is {SCORE}.")
    choice_a = random.choice(data)
    choice_b = random.choice(data)

    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Compare: {format_data(choice_a)}")
    print(VS)
    print(f"Against: {format_data(choice_b)}")
    guess = input("Who do you think has more followers. Type A or B :)\n> ").lower()
    following_a = choice_a["follower_count"]
    following_b = choice_b["follower_count"]

    if check_answer(following_a, following_b) == guess and LIVES != 0:
        SCORE +=1
        print(f"Correct! Current SCORE is {SCORE}.")
    elif check_answer(following_a, following_b) != guess and LIVES > 0:
        print("That is incorrect. You've lost one life.")
        LIVES -= 1
    else:
        print(f"Sorry, that's incorrect. Your final SCORE is {SCORE}.")
        GAME_OVER = True
