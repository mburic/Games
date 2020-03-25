import turtle
import winsound


# Create window
wn = turtle.Screen()
wn.title("PingPong")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops the windows from updating

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()  # turtle object
paddle_a.speed(0)  # speed of animation
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  #paddle dimension
paddle_a.penup()  # Turtle will move around the screen, but will not draw when its pen state is PENUP
paddle_a.goto(-377, 0) # paddle to start at -370



# Paddle B
paddle_b = turtle.Turtle()  # turtle object
paddle_b.speed(0)  # speed of animation
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  #paddle dimension
paddle_b.penup()  # Turtle will move around the screen, but will not draw when its pen state is PENUP
paddle_b.goto(370, 0) # paddle to start at -350



# Ball
ball = turtle.Turtle()  # turtle object
ball.speed(0)  # speed of animation
ball.shape("square")
ball.color("yellow")
ball.penup()  # Turtle will move around the screen, but will not draw when its pen state is PENUP
ball.goto(0, 0) # paddle to start at -350
# movement by 2 px:
ball.dx = 0.1
ball.dy = -0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 22, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor() # Return with the values of y coordinate
    y +=30
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor() # Return with the values of y coordinate
    y -=30
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor() # Return with the values of y coordinate
    y +=30
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor() # Return with the values of y coordinate
    y -=30
    paddle_b.sety(y)


# Keyboard binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # when press "w" call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")  # when press "s" call the function paddle_a_up
wn.onkeypress(paddle_b_up, "Up")  # when press "Up" call the function paddle_a_up
wn.onkeypress(paddle_b_down, "Down")  # when press "Down" call the function paddle_a_up


# Main game loop
while True:
    wn.update() # every time the loop run, it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('C://Users/MAURO/Desktop/MAURO/vjezbe/PYTHON/Projects/Games/Pong1/bounce1.wav', winsound.SND_ASYNC)

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        winsound.PlaySound('C://Users/MAURO/Desktop/MAURO/vjezbe/PYTHON/Projects/Games/Pong1/bounce1.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))
    

    # Paddle and ball collisions
    # Paddle B
    if (ball.xcor() > 350 and ball.xcor() < 360)  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(350)
        ball.dx *= -1
        winsound.PlaySound('C://Users/MAURO/Desktop/MAURO/vjezbe/PYTHON/Projects/Games/Pong1/bounce2.wav', winsound.SND_ASYNC)

    # Paddle A
    if (ball.xcor() < -357 and ball.xcor() > -367)  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-357)
        ball.dx *= -1
        winsound.PlaySound('C://Users/MAURO/Desktop/MAURO/vjezbe/PYTHON/Projects/Games/Pong1/bounce2.wav', winsound.SND_ASYNC)
