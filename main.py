import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

print("Made by Batuhan Utebay")
window = Screen()
window.title("Pong")
window.setup(800, 600)
window.bgcolor("black")
window.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
window.listen()
window.onkeypress(r_paddle.go_down, "Down")
window.onkeypress(r_paddle.go_up, "Up")

window.onkeypress(l_paddle.go_down, "s")
window.onkeypress(l_paddle.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    window.update()
    ball.move()
    if scoreboard.winner():
        game_is_on = False
        window.exitonclick()

    elif ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    elif ball.distance(r_paddle) < 50 and ball.xcor() < 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.restart()

    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.restart()

