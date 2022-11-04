from turtle import Turtle

STEP = 20
UP = 90

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.turtlesize(stretch_len=5)
        # self.color('white')
        self.setheading(UP)
        self.setpos(position)

    def up(self):
        self.forward(STEP)
    
    def down(self):
        self.backward(STEP)


    
