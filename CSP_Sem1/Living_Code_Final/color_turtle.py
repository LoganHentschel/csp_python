#change colors of a turtle turlte based on key press
#turtle must be turtle shape
#r is red, b is blue, g is green, c is black
import turtle 
screen = turtle.Screen()
# # # # # # #
def change_red():
   color_turtle.color('red')

def change_blue():
    color_turtle.color('blue')

def change_green():
    color_turtle.color('green') 

def change_black():
    color_turtle.color('black')

# # #

color_turtle = turtle.Turtle()
color_turtle.shape('turtle')

screen.onkeypress(change_red, 'r')
screen.onkeypress(change_blue, 'b')
screen.onkeypress(change_green, 'g')
screen.onkeypress(change_black, 'c')
screen.listen()


# # # # #
screen = turtle.Screen()
screen = turtle.mainloop()