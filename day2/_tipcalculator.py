'''Today's Final Project, a Tip Calculator'''

print("Welcome to the Tip Calculator!")
# The formula for a tip should be ( price / people ) * tip percentage (0.x) = result.
# To get both the full price and tip, multiply by 1.x where x is the tip percentage.
#Converts both into an INT for later.

BILL=float(
    input("What was the total bill?\n$ ")
    )
TIP_INPUT=float(
    input("How much of a tip would you like to give? This is a percentage. (eg. 10, 25, etc)\n")
    )
SPLIT=float(
    input("How many are splitting the bill? (Input 1 for none)\n")
    )
SPLIT2=float(BILL/SPLIT)
TIP=(TIP_INPUT/100.0)+1.0
TOTAL=round(
    (BILL/SPLIT)*TIP, 2
    )
TIPSOLO=round(float(TOTAL-(BILL/SPLIT)), 2)

print(f"Each person should pay: ${TOTAL}.")
print(f"Each person will pay ${SPLIT2}, with each person paying a ${TIPSOLO} tip.")
