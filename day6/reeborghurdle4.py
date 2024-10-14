'''The solution to Reeborg's World "Hurdle 4" level'''
# I didn't know you could use while loops in functions like here.
# Also remember that the code is read from top to bottom.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right() == True:
        move()  
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()
