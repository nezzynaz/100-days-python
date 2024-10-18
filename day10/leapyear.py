'''Function to figure out if a year is a leap year from the exercise'''

def is_leap_year(year):
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
