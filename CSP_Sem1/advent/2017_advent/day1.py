#check each number in that sequence. i
#if the number directly next to it is the same, add that number to a/the count. if index+1 == index?
#find the sum of all numbers that are the same as the number next to them

with open('inputs/day1.txt', 'r') as infile:
    data = infile.read()
print(data)

count = 0

#is data position 0 the same as data positon 1? 1 as 2? 2 as 3? and so on?
#data[0] == data[1]
#data[1] == data[2]
#data[2] == data[3]

for index in range(len(data)):
    if data[index] == data[index + 1]:
        count += int(data[index])

print(count)