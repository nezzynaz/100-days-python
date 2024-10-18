'''More notes on functions'''

# Another example of creating functions that create repeatable functionality.
def format_name(f_name, l_name):
    # How do you solve an issue where nothing is inputted or something is not quite right?
    if f_name == "" or l_name == "":
        # return (You can just return if theres not any value, skipping the whole process)
        return "No input" # This at least gives an indication that something went wrong.

    f_name_formatted = f_name.title()
    l_name_formatted = l_name.title()
    # return will change the output of the function to this.
    return f"{f_name_formatted} {l_name_formatted}"

output = format_name("NeZzY", "NaZ")
print(output)

# Return has benefits over print because it allows a function to be used as input
# for another function. For instance:

def function1(text):
    return text + text

def function2(text):
    return text.title()

# In this example, function1 is the input for function2.
NEWOUTPUT = function2(function1("HeLlO"))
print(NEWOUTPUT)
