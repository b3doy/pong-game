from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shapesize(stretch_len=300, stretch_wid=0.2)
        self.penup()
        self.setheading(90)
        self.setpos(0, 300)