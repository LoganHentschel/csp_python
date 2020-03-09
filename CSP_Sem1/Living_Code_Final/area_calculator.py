#area calculator
#cirlce, triangle, or rectangle
#ask for needed info (base, height, radius, 
#print answers to screen)

def circle_calc():
    #3.14 * radius squared/radius * radius
    global radius
    square = radius * radius
    area = 3.14*radius
    print("Your circle's area is", area)

def triangle_calc():
    #base * hiehgt / 2
    global base
    global hieght
    area = (base*height) / 2
    print("Your triangle's area is", area)

def rectangle_calc():
    #base * height
    global base
    global hieght
    area = base*height
    print("Your rectangle's area is", area)

# # # # # # #

shape_input = input('What shape do you want the area of - circle, rectangle, or triangle?:  ')

if shape_input == 'circle':
    radius = int(input('Please input the radius length of your shape:  '))
    circle_calc()
elif shape_input == 'rectangle':
    base = int(input('Please input the base length of your shape:  '))
    height = int(input('Please input the height length of your shape:  '))
    rectangle_calc()
elif shape_input == 'triangle': 
    base = int(input('Please input the base length of your shape:  '))
    height = int(input('Please input the height length of your shape:  '))
    triangle_calc()
else:
    print('Not an available shape, please try again')