'''Final project for day 3, building a clone of Treasure Island!'''
# ASCII ART Generator: https://ascii.co.uk/art

# You can use a backslash \ to escape a character in a string,
# useful when using doublequotes in strings where your brackets are singlequotes
# e.g. print('You\'re doing a great job "nezzy"')
# Using ''' allows for strings to go beyond one line.
print('''
    *Insert Awesome ASCII Art Here*
    Welcome to treasure island! Your mission is to find the treasure that's hidden here.
      ''')

FORK = input("The path forks to the left and the right, where do you go?\n").upper()

if FORK == "LEFT":
    RIVER = input('''You come across a river with a destroyed bridge, but another path
    leads down the river. Try to swim across or take the path?\n''').upper()
    if RIVER == "PATH":
        DOOR = input('''You find a village with multi-colored buildings, each with an enticing door.
        Do you pick the blue, yellow, or red door?\n''').upper()
        if DOOR == "BLUE":
            print("You open the door to a pack of hungry wolves. Game over.")
        elif DOOR == "RED":
            print("As you open the door, a fire trap activates and burns you. Game over.")
        elif DOOR == "YELLOW":
            print("The yellow door revealed a vault holding the treasure you seek. You Win!")
        else:
            print("I don't know what you're trying to do so... game over I guess?")
    elif RIVER == "SWIM":
        print("You were attacked by a shark in the river. Game Over.")
elif FORK == "RIGHT":
    print("You follow the path but end up falling into a trap. Game Over.")

print("This isn't meant to be a real game, just a test for the project. Thanks for playing!")
