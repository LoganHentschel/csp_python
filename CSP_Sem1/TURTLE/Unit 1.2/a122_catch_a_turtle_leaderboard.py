import turtle
import random as rand
import leaderboard as lb
# # # # #

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

### CREATING TURTLES ###
spot = turtle.Turtle()
score_writer = turtle.Turtle()
counter =  turtle.Turtle()

### VARIABLES ###
shape = "turtle"
shapesize = 2
fillcolor = "skyblue"
#
score = 0
font_setup = ("Arial", 30, "normal")
#
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

### SETTING VARIABLES ###
spot.shape(shape)
spot.shapesize(shapesize)
spot.fillcolor(fillcolor)
#
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-200,150)
#
counter.penup()
counter.hideturtle()
counter.goto(0,150)
### #### ###
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

### FUNCTIONS ###
def spot_clicked(x,y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        spot.hideturtle()
# x x x #
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.showturtle()
# x x x #
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
# x x x #
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


### EVENT EXECUTIONS ###
spot.onclick(spot_clicked)

# # # # #
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()