'''Letter Writing Program'''

PLACEHOLDER = "[name]"

with open("Input\\Names\\invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("Input\\Letters\\starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output\\ReadyToSend\\letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)

# Big takeaways:
# You can use an f string to name the file you want to create, as seen on line 13
# The strip function will remove the new line character, as seen on line 11
# My logic was correct throughout my initial attempt, and everything I didn't know is recorded here.
