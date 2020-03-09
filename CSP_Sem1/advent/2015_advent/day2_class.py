def get_dimensions(line):
    x1 = line.find('x')
    x2 = line.rfind('x')

    l = int(line[:x1])
    w = int(line[x1+1:x2])
    h = int(line[x2+1:])
    return(l,w,h)

def calculate_surface(l, w, h):
    return 2*l * 2*w * 2*h

def add_slack(l,w,h):
    return min(l*w,w*h,l*h)



with open('inputs/day2.txt') as infile:
    data = infile.readlines()

total_paper = 0

for line in data:
    line = line.strip()
    l,w,h = get_dimensions(line)
    total_paper += calculate_surface(l,w,h) + add_slack(l,w,h)


print(total_paper)
