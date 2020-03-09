import turtle
# # # # #

def draw_square(x,y,size):
    trtl.penup()
    trtl.goto(x,y)
    trtl.setheading(0)
    trtl.pendown()
    for _ in range(4):
        trtl.forward(size)
        trtl.right(90)

trtl= turtle.Turtle()

draw_square(0,0,100)
draw_square(-150,20,30)








# # # # #
screen = turtle.Screen()
screen.mainloop()