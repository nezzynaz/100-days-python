'''Exercise creating a "Who will pay the bill?" calculator'''
import random

FRIENDS = ["Friend 1", "Friend 2", "Friend 3", "Friend 4", "Friend 5"]

# Option 1 is using random.choice https://docs.python.org/3/library/random.html#random.choice
print(random.choice(FRIENDS))


#Option 2 is using randint to pull a number from the list.

FRIEND_NAME = random.randint(0, 4)
print(FRIENDS[FRIEND_NAME])
