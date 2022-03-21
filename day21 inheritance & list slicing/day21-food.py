from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")


    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)


#Slicing
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
#
# print(piano_tuple[1:5])
# print(piano_keys[::3])