infile = open('Inputs/day1.txt', 'r' )

data = infile.read()
infile.close()
count = 0
position_count = 0

#for element in iterable:
for char in data:
    if char == '(':
        count += 1
        position_count += 1
    else:
        count -= 1
        position_count += 1

    if count == -1:
        break
    
    #continue until num is -1, then find the location of that num
    
print(count)
print(position_count)