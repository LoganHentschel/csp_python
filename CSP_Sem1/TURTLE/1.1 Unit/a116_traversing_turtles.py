#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  Adds beginning quardinates for the turtle(s)
startx = 0
starty = 0

#used to create the box/square shape to separate the turtle shapes; go back to the line (according to the past and current coridinates) 
#and then continue the line/box pattern
for t in my_turtles:
	t.goto(startx, starty)
	t.right(45)     
	t.forward(50)

#Continuing the line/box pattern as previously mentioned; making sure to add 50 in order to keep it a strait line and not go bak to the same point as before
	startx = startx + 50
	starty = starty + 50

wn = trtl.Screen()
wn.mainloop()