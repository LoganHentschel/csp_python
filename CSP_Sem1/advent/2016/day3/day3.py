#In your puzzle input, how many of the listed triangles are possible?
#In a valid triangle, the sum of any two sides must be larger than the remaining side. 

with open('day3.in') as infile:
    data = infile.read().split('\n')

num = [[5, 10, 25], [25, 10, 5], [566, 477, 376], [575, 488, 365], [50, 18, 156]]

split_list = []
check = 0

for line in data:
    nums = line.split()
    split_list.append(nums)

for line in split_list:
    side_a = int(line[0])
    side_b = int(line[1])
    side_c = int(line[2])
    #
    side_1 = side_a + side_b #= side_c
    print(side_1, side_c)
    side_2 = side_a + side_c #= side_b
    print(side_2, side_b)
    side_3 = side_c + side_b #= side_a
    print(side_3, side_a)
    # # #
    if (side_1 > side_c) and (side_2 > side_b) and (side_3 > side_a):
       print('this one is a triangle')
       check += 1
       print(check)
    else:
        print('not triangle')
        print(check)

print('possible triangles:', check)