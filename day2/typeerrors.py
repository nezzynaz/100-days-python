'''Lesson on TypeErrors'''
# len(12345) is a type error
len("12345") # is a data type that the len() function accepts

string = "Hello"
integer = 4
float_example = 3.14
boolean = True

# the type function will say what kind of type a set of data is
print(type(string))
print(type(integer))
print(type(float_example))
print(type(boolean))

# Typecasting is how you turn one datatype into another
# the int() function turns a string into an integer

print(int("123") + int("456"))

# Also works with other datattypes

int()
float()
str()
bool()

# Test Problem: print("Number of letters in your name: " + len(input("enter your name")))
# The answer is to convert the integer created by len() into a string so it can be concatinated with the rest of the print.
#
# This converts the answer over one line
#print("Number of letters in your name: " + str(len(input("enter your name\n"))))

# The same program converted using variables instead, spaced out for better comprehension (teacher answer)
username = input("Enter your name\n")
length_name = len(username)
length_name_string = str(length_name)

print("Number of letters in your name: " + length_name_string)
