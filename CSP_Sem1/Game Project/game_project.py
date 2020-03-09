import turtle
import random
# # # # #
screen = turtle.Screen()
screen.title ("Bee Game - By Logan Hentschel & DeAndre Westbrook III ")
# # # #
counter =  turtle.Turtle()
timer = 20
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#
score = 0
font_setup = ("Arial", 30, "normal")
font_setup2 = ("Arial", 15, "normal")
#
collision = 'True'
collision_tolerance = 35
#
better_flower_true = 0
#
bee_img = 'bee.gif'
screen.addshape(bee_img)

flower_img = 'flower.gif'
screen.addshape(flower_img)

better_flower_img = 'better_flower.gif'
screen.addshape(better_flower_img)

touched_flower_img = 'touched_flower.gif'
screen.addshape(touched_flower_img)

# # # # 
Flower = turtle.Turtle()
Flower.shape(flower_img)
Flower.penup()
Flower.goto(30,-30)

Better_Flower = turtle.Turtle()
Better_Flower.shape(better_flower_img)
Better_Flower.penup()
Better_Flower.goto(-30,30)

Bee = turtle.Turtle()
Bee.shape(bee_img)
Bee.penup()
Bee.speed(0)

score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-250,-200)

final_writer = turtle.Turtle()
final_writer.speed(0)
final_writer.penup()
final_writer.hideturtle()

instructions_writer = turtle.Turtle()
instructions_writer.speed(0)
instructions_writer.penup()
instructions_writer.hideturtle()
instructions_writer.goto(-300,200)
instructions_writer.write("Arrow keys move the Bee!", font=font_setup2)

goals_writer = turtle.Turtle()
goals_writer.speed(0)
goals_writer.penup()
goals_writer.hideturtle()
goals_writer.goto(100,200)
goals_writer.write("Pink Flower = 5 points\nBlue Flower = 1 point", font=font_setup2)


counter.penup()
counter.speed(0)
counter.hideturtle()
counter.goto(-50,200)

# # #
def move_flower():
    new_xpos = random.randint(-200,200)
    new_ypos = random.randint(-150,150)
    Flower.hideturtle()
    Flower.goto(new_xpos, new_ypos)
    Flower.shape(flower_img)
    Flower.showturtle()

def move_better_flower():
    new_xpos = random.randint(-200,200)
    new_ypos = random.randint(-150,150)
    Better_Flower.hideturtle()
    Better_Flower.goto(new_xpos, new_ypos)
    Better_Flower.shape(better_flower_img)
    Better_Flower.showturtle()

def timer_move_flower():
    modu = timer%5
    dule = timer%3
    if modu == 0:
      move_flower()
    if dule == 0:
      move_better_flower()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def update_score_better():
   global score
   score += 5
   score_writer.clear()
   score_writer.write(score, font=font_setup)


def countdown():
  global timer, timer_up, score, collision
  counter.clear()
  if timer <= 0:
    collision = 'False'
    timer_up = True
    counter.write("Time's Up", font=font_setup)
    Bee.hideturtle()
    final_writer.goto (-150,0)
    final_writer.write ('Final Score:',font = font_setup)
    score_writer.goto(50,0)
    score_writer.write (score, font = font_setup)
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
    timer_move_flower()
  

def move_up():
    Bee.setheading(90)
    Bee.forward(40)
    detect_collision()

def move_down():
    Bee.setheading(270)
    Bee.forward(40)
    detect_collision()

def move_left():
    Bee.setheading(180)
    Bee.forward(40)
    detect_collision()

def move_right():
    Bee.setheading(0)
    Bee.forward(40)
    detect_collision()

def detect_collision():
    global better_flower_true
    global collision
    if collision == 'True':
      if Bee.distance(Flower.xcor(), Flower.ycor()) <= collision_tolerance: 
          flower_touched()
      if Bee.distance(Better_Flower.xcor(), Better_Flower.ycor()) <= collision_tolerance: 
          better_flower_touched()

def flower_touched():
    global score
    Flower.shape(touched_flower_img)
    update_score()
    move_flower()

def better_flower_touched():
  global score
  Better_Flower.shape(touched_flower_img)
  update_score_better()
  move_better_flower()



###
screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')

# # # # #
screen.listen()
screen.ontimer(countdown, counter_interval) 
screen.mainloop()