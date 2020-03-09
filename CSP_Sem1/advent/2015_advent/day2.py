infile = open('input/day2.txt', 'r')
lines = infile.readlines()
infile.close()

for line in lines:
    line = line.strip()
    first_x = line.find('x')
    second_x = line.rfind('x')

    length = line(:first_x)
    width = line(first_x+1:second_x)
    height = line(second_x+1:)

    print('Length: ', length, 'Width: ', width, 'Height: ', height)

