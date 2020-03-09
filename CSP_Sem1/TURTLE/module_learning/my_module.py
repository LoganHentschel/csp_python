def write_list_to_file(filename, list_name):
    outfile = open(filename, 'w')
    for item in list_name:
        outfile.write(item + '\n')

    outfile.close()

def read_list_from_file(filename):
    try:
        infile = open(filename, 'r')
        new_list = []
        for line in infile:
            new_list.append(line.strip())
        return new_list
    except:
        return []