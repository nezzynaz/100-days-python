'''Notes on the range() function.'''

# The range function helps you generate a range of numbers to loop through.
# The range function needs a for loop to function

# This will give all the numbers between 1 and 10, not including 10.
for number in range(1, 10):
    print(number)

# By adding another comma you can adjust the step of each number
for number in range(1, 10, 2):
    print(number)

# Solving Gauss' math problem using python.
total = 0
for number in range (1, 101):
    total += number
print(total)
