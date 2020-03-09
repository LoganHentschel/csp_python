import turtle
#####

turt = turtle.Turtle()

color = input('Hello! What color would you like for the square?:  ')
side = int(input('And what side length?:  '  ))
print('Thank you! Now generating...')

turt.begin_fill()
turt.color(color, color)

turt.forward(side)
turt.left(90)
turt.forward(side)
turt.left(90)
turt.forward(side)
turt.left(90)
turt.forward(side)
turt.left(90)

turt.end_fill()

'''turt.shape('square')
turt.shapesize(side)'''

print('Square Generated.')

#####
screen = turtle.Screen()
screen.mainloop()
######################
''' Input challenge:
-ask user for color
-ask user for a side length
-draw a square of that side length w/ that color'''