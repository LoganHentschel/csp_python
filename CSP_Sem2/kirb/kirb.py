# # # # # IMPORTS # # # # #
import turtle

# # # # # SCREEN STUFF # # # # # 
screen = turtle.Screen()

# # # # # SPRITES # # # # #
# FLOOR #
floor = turtle.Turtle()
floor.hideturtle()
floor.shape('square')
floor.penup()
floor.goto(0,-25)
floor.showturtle()

# KIRBY #
kirby_img = 'kirby_img.gif'
screen.addshape(kirby_img)
Kirby = turtle.Turtle()
Kirby.penup()
#Kirby.goto(0, 250)
Kirby.shape(kirby_img)
Kirby.speed(0)

# # # # # FUNCTIONS # # # # #
def move_left():
    x = Kirby.xcor()
    Kirby.setx(x - 20)

def move_right():
    x = Kirby.xcor()
    Kirby.setx(x + 20)

def jump_up():
    global speed_y, collision
    #
    y = Kirby.ycor()
    Kirby.sety(y + 40)
    #
    collision = 'False'
    falling()

def collision_detection():
    global collision
    if Kirby.distance(floor.xcor(), floor.ycor()) <= collision_tolerance: 
        print('Collided')
        collision = 'True'

def falling():
    global speed_y
    #
    print('FALLING')
    while collision == 'False':
        speed_y -= 1
        y = Kirby.ycor()
        Kirby.sety(y+speed_y)
        collision_detection()

# # # # # VARIABLES # # # # #
speed_y = 0

collision = 'False'
collision_tolerance = 15

# # # # # KEYBINDING # # # # # 
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')
screen.onkeypress(jump_up, 'Up')

# # # # # SCREEN STUFF # # # # # 
screen.listen()
screen.mainloop()