from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Wich turtle win the race? Enter a color: ")
print(user_bet)
colors = ("red", "orange", "yellow", "green", "blue", "purple")
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle winner")
            else:
                print(f"You've Lost! The {winning_color} turtle winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()