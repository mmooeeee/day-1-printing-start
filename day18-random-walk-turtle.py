#from turtle import Turtle, Screen
import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

#  colours = ["silver", "midnight blue", "dark green", "goldenrod", "pale violet red", "dark slate blue", "navy",
#            "light sky blue", "indian red", "red"]

direction = [0, 90, 180, 270]
tim.pen(pensize=10)
tim.speed(5)

for i in range(200):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(direction))







# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


# for i in range(3):
#     tim.forward(50)
#     tim.right(120)
#
# for i in range(4):
#     tim.forward(50)
#     tim.right(90)
#
# for i in range(5):
#     tim.forward(50)
#     tim.right(72)


# screen = Screen()
# screen.exitonclick()