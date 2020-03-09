import turtle
import random 

# # # # # # #
screen = turtle.Screen()
screen.setup(600,650)
# # #
alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
font = ['Arial', 20, 'normal']

letter_list = []
turtle_list = []

# # #
background_img = 'background.gif'
screen.bgpic(background_img)

apple_img = 'apple.gif'
screen.register_shape("apple.gif")
#apple = turtle.Turtle()
#apple.shape(apple_img)

# # #
def handle_key(key):
   print(key, 'pressed')
   if key in letter_list:
       index = letter_list.index(key)
       letter_list.pop(index)
       current_apple = turtle_list.pop(index)
       falling_apple(current_apple)

def falling_apple(apple):
    apple.goto(apple.xcor(),-200)
    random_apple(apple)

def random_apple(apple):
    #moves to new location
    apple.hideturtle()
    apple.speed(0)
    x = random.randint(-250, 250)
    y = random.randint(-150,200)
    apple.goto(x,y)
    apple.showturtle()
    apple.speed(3)
    
    #Assigns new letter
    new_letter = random.choice(alphabet)
    alphabet.remove(new_letter)
    letter_list.append(new_letter)
    turtle_list.append(apple)
    apple.write(new_letter.upper(), font=font)
    print(letter_list)
# # #

for letter in alphabet:
    screen.onkeypress(lambda l = letter: handle_key(l), letter)

for _ in range(5):
    apple = turtle.Turtle('apple.gif')
    apple.penup()
    random_apple(apple)

print(letter_list)
print(len(turtle_list))

# # # # # # #
screen.listen()
screen.mainloop()