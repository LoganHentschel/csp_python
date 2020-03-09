with open('day1.in') as infile:
    data = infile.read().split('\n')

answer = 0
list1 = []

for line in data: 
    line = int(line)
    if line in list1:
        print('REPEAT', line)
    list1.append(answer)


