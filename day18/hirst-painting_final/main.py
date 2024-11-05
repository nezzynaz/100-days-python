'''Hirst Painting Color Extraction using python turtle'''

# import colorgram
import random
import turtle as t

# rgb_colors = []
# colors = colorgram.extract('day18/hirst-painting/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

colorlist = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
screen = t.Screen()

screen.bgcolor("gainsboro")
screen.colormode(255)
screen.setup(600, 600)
tim.shape("arrow")

tim.width(50)
tim.speed(0)
tim.penup()
dot_size = 20
dot_spacing = 50

start_x, start_y = -250, -250
tim.goto (start_x, start_y)

for row in range(10):
    for col in range(10):
        tim.dot(dot_size, random.choice(colorlist))
        tim.forward(dot_spacing)
    tim.backward(dot_spacing * 10)
    tim.left(90)
    tim.forward(dot_spacing)
    tim.right(90)

screen.mainloop()
# screen.exitonclick()
