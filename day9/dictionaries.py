'''Notes on Dictionaries'''
# Dictionaries are lists that store key value pairs, such as a word and its definition.


programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing the same thing over and over again.",
                          }

# A key error may happen if you try to pull out a key that doesn't exist.
# Another common mistake is using the wrong data type when you "fetch" a key.
print(programming_dictionary["Bug"])

# You can create an empty dictionary with
empty_dictionary = {}

# To add to a dictionary, you can put in something like this.
empty_dictionary["Loop"] = "The action of doing the same thing over and over again."

# And wipe a dictionary by using the same code as creating an empty dictionary
empty_dictionary = {}

# You can redefine a value in a dictionary by fetching it and setting it to something else.
programming_dictionary["Bug"] = "An insect"

# printing a dictionary in a for loop will print all the keys, but not their values.
for i in programming_dictionary:
    print(i)
    # print(programming_dictionary[i]) #This will allow you to print the values as well.

programming_dictionary.items() # An easier way of doing line 30 is with this instead.

# Lists and Dictionaries can be nested in each other, making the structure complex.

""" travel_log = {
    "France": ["Paris", "Dijon", "Little"],
    "Germany": "Berlin",
}

# This prints the second item in the list.
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1]) """

# A dictionary inside a dictionary, inside a dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])
