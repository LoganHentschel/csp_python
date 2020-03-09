import turtle
# # #

moving = turtle.Turtle()
moving.shape('turtle')
moving.penup()
moving.speed(0)

screen = turtle.Screen()

def move_up():
    moving.setheading(90)
    moving.forward(30)

def move_down():
    moving.setheading(270)
    moving.forward(30)

def move_left():
    moving.setheading(180)
    moving.forward(30)

def move_right():
    moving.setheading(0)
    moving.forward(30)
###
screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')

# # #
screen.listen()
screen.mainloop()