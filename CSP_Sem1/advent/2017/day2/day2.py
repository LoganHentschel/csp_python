with open('day2.in') as infile:
    data = infile.read().split('\n')

line_list = []

for line in data:
    line_list.append(line.split())

answer = 0

for line in line_list:
    char_list = []
    maxi = 0
    mini = 0

    for char in line:
        char = int(char)
        char_list.append(char)

        maxi = max(char_list)
        mini = min(char_list)
        
        check = maxi-mini
    answer += check

print('answer', answer)

