with open('day1.in') as infile:
    num = infile.read()
#num = '1111'
total = 0

for index in range(len(num)-1):
    if num[index] == num[index+1]:
        total += int(num[index])
if num[0] == num[-1]:
    total+=int(num[0])

print(total)