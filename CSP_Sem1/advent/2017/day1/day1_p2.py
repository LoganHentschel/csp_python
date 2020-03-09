'''the digit halfway around the circular list. 

For example:
1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.'''
#################

num = '1212'
halfway = len(num)/2
total = 0

for index in range(len(num)-1):
    if num[index] == num[index+1]:
        total += int(num[index])
if num[0] == num[-1]:
    total+=int(num[0])

print(total)