from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 55, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.red = 0
        self.blue = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.board()

    def board(self):
        self.setpos(-100, 200)
        self.write(self.blue, move=False, align=ALIGNMENT, font=FONT)
        self.setpos(100, 200)
        self.write(self.red, move=False, align=ALIGNMENT, font=FONT)
        
    def update_right_score(self):
        self.clear()
        self.red += 1
        self.board()
    
    def update_left_score(self):
        self.clear()
        self.blue += 1
        self.board()

    def game_over(self):
        self.goto(0, 0)
        if self.red == 10:
            self.write(f"Game Over! red is the Winner", move=False, align=ALIGNMENT, font=("courier", 24))
        else:
            self.write(f"Game Over! blue is the Winner", move=False, align=ALIGNMENT, font=("courier", 24))