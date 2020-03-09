import turtle
# # # # #
time = 0
timer_running = 'False'

font_setup = ("Arial", 30, "normal")
font2_setup = ("Arial", 20, "normal")

# # #
start = turtle.Turtle()
start.speed(0)
start.penup()
start.goto(-200, 100)
start.shape('circle')
start.shapesize(2)

start_text = turtle.Turtle()
start_text.hideturtle()
start_text.speed(0)
start_text.penup()
start_text.goto(-175,90)
start_text.write("Start", font=font2_setup)

# # #
stop = turtle.Turtle()
stop.speed(0)
stop.penup()
stop.goto(-200, 50)
stop.shape('circle')
stop.shapesize(2)

stop_text = turtle.Turtle()
stop_text.hideturtle()
stop_text.speed(0)
stop_text.penup()
stop_text.goto(-175,40)
stop_text.write("Stop", font=font2_setup)

# # #
reset = turtle.Turtle()
reset.speed(0)
reset.penup()
reset.goto(-200, 0)
reset.shape('circle')
reset.shapesize(2)

reset_text = turtle.Turtle()
reset_text.hideturtle()
reset_text.speed(0)
reset_text.penup()
reset_text.goto(-175,-10)
reset_text.write("Reset", font=font2_setup)

# # #
stopwatch_text = turtle.Turtle()
stopwatch_text.hideturtle()
stopwatch_text.speed(0)
stopwatch_text.penup()
stopwatch_text.goto(-200,150)
stopwatch_text.write("Stopwatch", font=font_setup)

# # #
counter = turtle.Turtle()
counter.hideturtle()
counter.speed(0)
counter.hideturtle()
counter.penup()
counter.goto(0,150)

### ##### ### ##### ###
def count_up():
    global time
    global timer_running
    time = round(time + 0.1, 1)
    counter.clear()
    counter.write(time, font=font_setup)
    if timer_running == 'True':
        screen.ontimer(count_up, 100)

def start_button_clicked(x,y):
    global timer_running
    if timer_running == 'False':
        screen.ontimer(count_up, 100)
        timer_running = 'True'

def stop_button_clicked(x,y):
    global timer_running
    timer_running = 'False'

def reset_button_clicked(x,y):
    global time
    stop_button_clicked(x,y)
    counter.clear()
    time = 0
    counter.write(time, font=font_setup)

### ### ### ### ###
start.onclick(start_button_clicked)
reset.onclick(reset_button_clicked)
stop.onclick(stop_button_clicked)

# # # # #
screen = turtle.Screen()
screen.mainloop()
