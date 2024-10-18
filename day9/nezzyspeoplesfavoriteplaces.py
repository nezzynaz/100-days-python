'''Favorite Places practice program. The first program I ideated and created from scratch.'''
import sys

places = {}

def placeinput():
    inputting = True

    while inputting:
        name = input("What is your name? \n> ")
        place = input("What is your favorite place? \n> ")
        places[name] = place
        quitinputting = input("Add another entry? yes or no. \n> ").lower()

        if quitinputting == "no":
            inputting = False
            print("Ok, returning to main menu.")
        elif quitinputting == "yes":
            print("Alright, who are we adding next?")
        else:
            print("Invalid input.")

def showplaces(place_dict):
    for i in place_dict:
        name = i
        place = place_dict[i]
        print(f"- {name}'s favorite place is {place}.")


def main():
    online = True
    while online:
        menu = input('''Welcome to Nezzy's People's Favorite Places. Type view to find all the places, or input to put new places in, or exit to quit. \n> ''').lower()
        if menu == "view":
            if bool(places) is False:
                print("There are no places. Input some places!")
            elif bool(places) is True:
                print("Here are all of Nezzy's People's Favorite places:")
                # print(places)
                showplaces(places)
        elif menu == "input":
            placeinput()
        elif menu == "exit" or "quit":
            online = False
            print("Thank you for using Nezzy's peoples favorite places. Goodbye!")

# First time using this. It runs the program if ran from console, but also allows for modularity.
#if __name__ == "__main__":
#    main()

# Revision of above, adding the option to [control+c] to exit.
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit(0)
