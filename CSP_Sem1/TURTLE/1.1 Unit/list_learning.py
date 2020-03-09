import turtle
# # #
turtle_list =  []
length_list = []


decision = 'yes'

while decision == 'yes':
    color = input("Enter a color:  ")
    heading = int(input("Enter a heading:  "))
    length = int(input("Enter a length:  "))

    #
    t = turtle.Turtle()
    t.color(color)
    t.setheading(heading)
    turtle_list.append(t)
    length_list.append(length)
    
    #
    decision = input('Wold you like to make another tuurtle?:  ')

###########################
#for element in iterab;e:

for index in range(len(turtle_list)):
    turtle_list[index].forward(length_list[index])

#for turt in turtle_list:
    #turt.forward(50)



# ## # ## #
screen = turtle.Screen()
screen.mainloop()
# # #