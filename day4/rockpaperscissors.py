'''Making a simple rock, paper, scissors game!'''
import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

PLAYER = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
HAND_SIGNS = [Rock, Paper, Scissors]
CPU = random.randint(0, 2)

CPU_CHOICE = HAND_SIGNS[CPU]
print(f"Computer chose {CPU_CHOICE}")

# The hardest part of this assignment was the logic. I should use a flowchart in the future.
# This logic was really hard to figure out, but essentially it checks if the player score
# is higher than the CPUs, and also handles various exceptions that may exist.
if PLAYER == 0 and CPU == 2:
    print("You win!")
elif PLAYER >= 3:
    print("Invalid number!")
elif CPU > PLAYER:
    print("You lose!")
elif PLAYER > CPU:
    print("You win!")
elif CPU == PLAYER:
    print("It's a draw!")
elif CPU == 2 and PLAYER == 0:
    print("You lose!")
