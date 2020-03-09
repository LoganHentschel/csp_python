#square drawing turtle
#make turtle draw 5 squares
#squares all share left-hand corner
#loops must be used
import turtle

# # # # #
def square_maker():
    global currant_squares
    sides = 0
    while sides < 4:
        square_turtle.forward(forward)
        square_turtle.right(90)
        sides += 1
    currant_squares += 1
# # # 
square_turtle = turtle.Turtle()
square_amount = 5
currant_squares = 0
forward = 50

# # #
while currant_squares < square_amount:
    square_maker()
    forward += 50

# # # # #
screen = turtle.Screen()
screen = turtle.mainloop()