import math as math

with open('day1.in') as infile:
    data = infile.read().split('\n')

'''answer = 0

for line in data:
    num = int(line)
    num = num/3
    num = math.floor(num)
    num = num-2
    answer += num

#~~~~~~~~~~~~~#
#different, better/easier method to solve!
nums = [int(num) for num in data]

fuels = [num // 3 - 2 for num in nums]

#print(sum(fuels))    
#sum() can add up entire list of numbers!'''
# ----------------------------- #
#each fuel needs to go thourgh the same equation as the module: take the list of fuels & run them through a system that calculates each
#fuel_fuels = [num // 3 - 2 for num in mod_fuels]

nums = [int(num) for num in data]
mod_fuels = [num // 3 - 2 for num in nums] #original add up of fuels

fuel_list = []

for num in mod_fuels:
    fuel_list.append(num)
    less = (num // 3) - 2
    fuel_list.append(less)

    while less > 0: 
        less = less // 3 - 2
        if less > 0:
            fuel_list.append(less)

print(len(fuel_list), sum(fuel_list))