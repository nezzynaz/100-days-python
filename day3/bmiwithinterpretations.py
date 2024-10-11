'''A more advanced BMI Calculator Exercise'''

WEIGHT = 85
HEIGHT = 1.85

BMI = WEIGHT / (HEIGHT ** 2)

# Comparison operators will be the death of me.
if BMI < 18.5:
    print("Underweight.")
elif BMI >= 18.5 < 25:
    print("Normal Weight")
elif BMI >= 25:
    print("Overweight")
