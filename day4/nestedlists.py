'''Notes on Nested Lists in Python'''
# An "Index Error" is when you try to find something that is outside your list range.
# For instance, if you try to find the last item of this list..
fruits = ["apple", "pear", "banana"]
# Through using the len() function, it will say theres 3 items, even though "banana" is technically 2.
fruit_length = len(fruits)
# But by shrinking it -1, it will find the correct value.
print(fruits[fruit_length - 1])

# Lists may also be put into "Nested" lists.
# Here, I've made another list.
vegetables = ["Spinach", "Potato", "Tomato"]

# And this will combine the lists together in a nested list
# Keep in mind, the order of the list matters.
grown_foods=[fruits, vegetables]

# Notice how it prints with two brackets, and seperates both lists.
print(grown_foods)

# When you print out a specific  item from a nested list,
# you'll first specify which list, then the item you want.
print(grown_foods[1][1])
#This will print out the second item from the second list.
