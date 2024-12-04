'''An alternate way to open files in python using the "with" keyword'''

# The with statement is used to simplify the use of common resources like files
# https://www.geeksforgeeks.org/with-statement-in-python/

with open(file="day24/data.txt", mode="a") as file:
    # contents = file.read()
    file.write("\nAppending text to this file!")
    # print(contents)
    file.close()

