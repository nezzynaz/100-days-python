'''Today is about accessing and writing to the filesystem using python, and its implementation in code!'''

# The built in "open" method lets you open a file!
file = open("day24/data.txt") 
# This will input the data as a variable

contents = file.read()
# The read method returns the contents of the file as a string

print(contents)
file.close()
# Closes the file manually, which saves resources akin to closing a tab in a browser.

# Check out main2.py to see a more simpler verison of writing this.
