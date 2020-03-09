import turtle
###########################
# ATTEMPT TO NUMBER EACH SQUARE

##########################
pen = turtle.Turtle()

row_num = int(input("Enter desired number of rows:   "))
colm_num = int(input("Enter the desired number of columns:   "))

pen.speed(0)

row = 0
colm = 0
grid_size = 50

while (row < row_num):
    #
    while (colm < colm_num):
        print(row,colm)
        pen.penup()
        pen.goto(colm*50,row*-50)
        pen.pendown()
        ### draw square @ location ###
        leg = 0 
        while leg < 4:
            pen.forward(grid_size)
            pen.right(90)
            leg += 1
        colm += 1
    colm = 0
    row += 1 


###################
screen = turtle.Screen()
screen.mainloop()