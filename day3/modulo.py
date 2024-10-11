'''Notes on a Modulo/Modulus'''
# The modulo operator % will find the remainder after division. 10 % 5 = 0 for instance.

VALUE = int(input("What number do you wish to check?"))

if VALUE % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")
