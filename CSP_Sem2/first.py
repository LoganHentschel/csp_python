'''
a = 'egg'
b = 'biscuit'
print("Hello ", a,' ', b,"! You just delved into python.", sep = '')

# convert all lowercase letters to uppercase letters and vice versa
def swap_case(s):
    swaped = ''
    for char in s:
        if char.isupper():
            char = char.lower()
            swaped = swaped + char
        elif char.islower():
            char = char.upper()
            swaped = swaped + char
        else:
            swaped = swaped + char
    return swaped

s = input()
result = swap_case(s)
print(result)

# Complete the solve function below.
def solve(s):
    num = 0
    solved = ''
    for char in s:
        num += 1
        if char == ' ':
            num = 0
        elif num == 1:
            char = char.upper()
            print(char)
        solved = solved + char   
    print(solved)
    return solved

s = input()
result = solve(s)

# Given a number variable, perform the following conditional actions:
# If  is odd, print Weird 
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

n = int(input().strip())

if (n % 2) == 0: #EVEN
    if n in range(2,6):
        print('Not Weird')
    elif n in range(6,21):
        print('Weird')
    elif n > 20:
        print('Not Weird')
else: #ODD
    if n > 20:
        print('Not Weird')
    else:
        print('Weird')
'''
#You are given the year, and you have to write a function to check if the year is leap or not.
#Note that you have to complete the function and remaining code is given as template.

year = int(input())
is_true = False

if (year % 4) == 0:
    is_true = True
    if  year % 100 == 0:
        if year % 400 == 0:
            is_true = True
        else:
            is_true = False
    
if is_true == 'True':
    print('True')
else:
    print('False')


#2000 2400 
#1800 1900 2100 2200 2300 2500
