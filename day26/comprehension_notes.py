'''Notes on using list comprehension in python!'''

# List comprehension allows you to create lists in a simple and efficient way.

# A basic example of name comprehension.
# name = "Nezzy"
# letters_list = [letter for letter in name]

# Another example of list comprehension.
#num = range(1, 5)
#num_list = [digit+1 for digit in num]

# https://www.w3schools.com/python/ref_dictionary_items.asp





# Testing conditional usage in comprehension. Notice how built-in functions are embedded.
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
cap_names = [name.upper() for name in names if len(name) > 5]

print(cap_names)
