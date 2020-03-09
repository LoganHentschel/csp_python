#turtle size should increase when spacebar is pressed; size 1-5, increasing; should go back to size 1 after size 5
import turtle
screen = turtle.Screen()
# # # # #
def size_change():
    global current_size
    if current_size == 5:
        current_size = 0
    size_turtle.shapesize(current_size+1)



# # #
size_turtle = turtle.Turtle()
current_size = 0


screen.onkeypress(size_change, 'space')
screen.listen()

# # # # #
screen = turtle.mainloop()