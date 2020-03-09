import turtle
# # # # #
turt = turtle.Turtle()
# # #

color = input('Hello! What color would you like for the shape?:  ')
length = int(input('And what side length?:  '  ))
sides = int(input('Now how many sides - keep 3 or more!:  '))
print('Thank you! Now generating...')
# #
count = 0
turn = 360/sides

turt.speed(0)

turt.begin_fill()

turt.color(color, color)

while (count < sides):
    turt.forward(length)
    turt.left(turn)
    count = count+1

turt.end_fill()

# #
print('Shape Generated.')
# # # # #
screen = turtle.Screen()
screen.mainloop()