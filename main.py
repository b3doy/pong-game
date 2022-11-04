from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from line import Line
import time

# Setup the screen
layar = Screen()
layar.bgcolor('black')
layar.setup(width=800, height=600)
layar.title('Pong')
layar.tracer(0)

# Assign the paddle
red = Paddle((350, 0))
red.color('red')
blue = Paddle((-350, 0))
blue.color('blue')

# Assign the ball
ball =  Ball()

# Assign the score
score = Score()

line = Line()


# Assign the control
layar.listen()
# Control of the right paddle:
layar.onkey(red.up, "Up")
layar.onkey(red.down, "Down")
# Control of the left paddle:
layar.onkey(blue.up, "w")
layar.onkey(blue.down, "s")

# keep game on
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    layar.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with the paddle
    if ball.distance(red) < 50 and ball.xcor() > 320 or ball.distance(blue) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # detect if the ball goes out of bounds behind the right_paddle
    if ball.xcor() > 390: 
        ball.reset_pos()
        score.update_left_score()
    # detect if the ball goes out of bounds behind the left_paddle
    if ball.xcor() < -390:
        ball.reset_pos()
        score.update_right_score()
    # if reach certain score then the game is over
    if score.blue == 10 or score.red == 10:
        game_on = False
        score.game_over()
        
        
        

layar. exitonclick()