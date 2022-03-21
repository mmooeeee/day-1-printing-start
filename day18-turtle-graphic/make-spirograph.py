import turtle as t
import random

tim = t.Turtle()

tim.speed(30)
t.colormode(255)

def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.heading()
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)
        # tim.left(10)

draw_spirograph(3)



screen = t.Screen()
screen.exitonclick()