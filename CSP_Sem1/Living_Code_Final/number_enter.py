#Python 1: ask user to ente number - ask user to input that many numbers 
#- each number added to a list - once all numbers have been inputed, list min max and average

number_list = []

num_check = 0
average = 0
list_amount = 0

number_of_numbers = int(input('Please enter a number:  '))

while num_check < number_of_numbers:
    number_list.append(int(input('Now please enter a number until your previous number has been met:  ')))
    num_check += 1
    print('You have inputed', num_check, 'out of', number_of_numbers)

min_list = min(number_list)

max_list = max(number_list)

#average is all numbers added and then divided by number of numbers
for num in number_list:
    list_amount += num
average = list_amount/number_of_numbers

print('Your minimumm is', min_list,', Your maximum is', max_list,', And your average is', average, )