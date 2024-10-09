'''Notes on Number Manipulation and F Strings'''

bmi = 84 / 1.65 ** 2
print(bmi)

# Flooring a number is a term for removing all remaining decimal places
# Flooring it to its whole number
# Converting the float into an int will do this, but will not round the number.

print(int(bmi))

# Rounding will round the number, bringing the number either up or down to the nearest whole number.

print(round(bmi))

# You can also round to a certain decimal place, keeping it a float. Great for finance work.

print(round(bmi, 2))

# Assignment operators allow us to accumulate results of calculations.
# Assignment operators include:
# +=
# -=
# *=
# /=

score = 0
score += 1
winning = True
print(score)

# F strings allow us to insert a variable of expression into a string.
# It's done by adding an f in front of a string, which allows values to be inserted into a string.

print(f"Your score is {score}, you are winning is {winning}!")
