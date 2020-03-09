''' draw a picture with turtle:
draw (2) pictures that describe your feelings about this beginning of the school year time frame
plan it on paper. make sure to have loops for repeating processes, conditions, ect.
**due tueday the 24th'''
# # # # # # # # # #
import turtle
### ### ### ### ###

head = turtle.Turtle()
left_arm = turtle.Turtle()
right_arm = turtle.Turtle()
rock = turtle.Turtle()
time = turtle.Turtle()
second = 'no'
# # #
head.speed(0)
left_arm.speed(0)
right_arm.speed(0)
rock.speed(0)

time.hideturtle()

# Will create whole set of lines induvidually/slight lopping; can create functions n loops from there

''' RECTANGLE HEAD '''
head.forward(100)
head.left(90)
head.forward(50)
head.left(90)
head.forward(100)
head.left(90)
head.forward(50)
#
head.hideturtle()


'''LEFT SIDE OF BODY '''
left_arm.penup()
left_arm.right(90)
left_arm.backward(20)
left_arm.right(45)
left_arm.pendown()
#
left_arm.forward(30)
left_arm.right(135)
left_arm.forward(75)
left_arm.left(90)
left_arm.forward(10)
left_arm.left(90)
left_arm.forward(100)
left_arm.left(135)
left_arm.forward(25)
left_arm.right(135)
left_arm.forward(15)
left_arm.right(15)
left_arm.forward(50)
left_arm.left(45)
left_arm.forward(50)
left_arm.right(120)
#
left_arm.forward(25)
left_arm.left(90)
left_arm.forward(10)
left_arm.left(90)
left_arm.forward(45)
left_arm.left(120)
#
left_arm.forward(65)
left_arm.right(45)
left_arm.forward(50)
left_arm.right(75)
left_arm.forward(50)
left_arm.hideturtle()

''' RIGHT SIDE OF BODY '''
right_arm.penup()
right_arm.forward(100)
right_arm.left(90)
right_arm.forward(20)
right_arm.right(135)
right_arm.pendown()
#
right_arm.forward(30)
right_arm.left(135)
right_arm.forward(75)
#
right_arm.right(90) 
right_arm.forward(10)
right_arm.right(90)
right_arm.forward(100)
right_arm.right(135)
right_arm.forward(25)
right_arm.left(135)
right_arm.forward(15)
right_arm.left(15)
right_arm.forward(50)
right_arm.right(45)
right_arm.forward(50)
right_arm.left(120)
# 
right_arm.forward(25)
right_arm.right(90)
right_arm.forward(10)
right_arm.right(90)
right_arm.forward(45)
right_arm.right(120)
#
right_arm.forward(65)
right_arm.left(45)
right_arm.forward(50)
right_arm.left(75)
right_arm.forward(55)
#
right_arm.hideturtle()


''' MOVE TURTLE TO ROCK POSITION '''
rock.penup()
rock.left(90)
rock.forward(75)
rock.left(90)
rock.forward(25) 
rock.pendown()
rock.right(180)


''' DRAW ROCK '''
### xxx ###
rock.begin_fill()
rock.color('black', 'gray')
### xxx ###
rock.forward(200)
rock.circle(25,90)
rock.forward(30)
rock.circle(50, 180)
#
rock.penup()
rock.forward(15)
rock.pendown()
#
rock.right(180)
rock.circle(50, 180)
#
rock.penup()
rock.forward(15)
rock.pendown()
#
rock.right(180)
rock.circle(50, 210)
rock.left(60)
rock.forward(75)
### xxx ###
rock.end_fill()
### xxx ###


''' DRAW SHAKE SQUIGGLES '''

''' ~~~~~~~~~~~~~~~~~ SECOND PICTURE ~~~~~~~~~~~~~~~~~ '''
second = input("Move on to next picture?: ")

if second == 'yes':
    turtle.clearscreen()
    ''' DRAW ROCK '''
    rock.reset()
    rock.penup()
    rock.right(90)
    rock.forward(100)
    rock.left(90)
    rock.backward(25)
    rock.pendown()
    ### xxx ###
    rock.begin_fill()
    rock.color('black', 'gray')
    ### xxx ###
    rock.forward(200)
    rock.circle(25,90)
    rock.forward(30)
    rock.circle(50, 180)
    #
    rock.penup()
    rock.forward(15)
    rock.pendown()
    #
    rock.right(180)
    rock.circle(50, 180)
    #
    rock.penup()
    rock.forward(15)
    rock.pendown()
    #
    rock.right(180)
    rock.circle(50, 210)
    rock.left(60)
    rock.forward(75)
    ### xxx ###
    rock.end_fill()
    ### xxx ###

    # ''' DRAW LEGS AGAIN ''' #
    #left leg#
    rock.right(135)
    rock.forward(75)
    rock.left(90)
    rock.forward(50)
    rock.right(90)
    rock.forward(25)
    rock.left(90)
    rock.forward(10)
    rock.left(90)
    rock.forward(35)
    rock.left(90)
    rock.forward(50)
    rock.right(90)
    rock.forward(75)
    #position right leg#
    rock.right(45)
    rock.forward(50)
    rock.right(45)
    rock.forward(75)
    rock.right(15)
    rock.forward(60)
    rock.left(90)
    rock.forward(25)
    rock.left(90)
    rock.forward(10)
    rock.left(90)
    rock.forward(15)
    rock.right(90)
    rock.forward(50)
    rock.left(15)
    rock.forward(70)

  
# # # # # # # # # # 
screen = turtle.Screen()
screen.mainloop()