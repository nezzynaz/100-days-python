'''How to make a docstring in a function'''

# To make a docstring in a function, you want to make three """ on the first line of
# a function after it's defined.
# The """ can be used as a multi-line comment, but isn't advised since it can cause issues.
# It's main use is with docstrings.

def is_leap_year(year):
    """Figures out if the inputted year is a leap year."""
    leap = False
    # Turns out, you only need to figure out the remainder, not the division as well.
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

print(is_leap_year(2000))

# VS code can also generate a docstring template.

def myfunction(text):
    """Doubles the string.

    Args:
        text (string): Hello.

    Returns:
        String: Hellohello
    """
    return text + text

print(myfunction("Hello"))
