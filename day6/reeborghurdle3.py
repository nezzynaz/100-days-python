'''The solution to Reeborg's World "Hurdle 3" level'''

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()