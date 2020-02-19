#calling the data file
path = 'data_files/311_CSV_Raw_Data.csv'

#opening & reading the data from the file - splitting the data at each new line
with open(path) as f:
    data = f.read().split('\n')

# # #
#variable list
time_list = []
temp1_list = []
temp2_list = []
counter = 0

#going through each line of data - splitting this line farther to isolate each specific data variable
for line in data[1:]:
    split_line = line.split(',')
    #turning the data from strings into numbers, then adding the types of data to their respective lists
    for var in split_line:
        var = float(var)
        counter += 1
        if counter == 1:
            time_list.append(var)
        elif counter == 2:
            temp1_list.append(var)
        elif counter == 3:
            temp2_list.append(var)
            counter = 0

''' 
#better way to sort out the data...
for line in data[1:]:
    split_line = line.split(',')
###
    time_list.append int(var[0])
    temp1_list.append(float(var[1]))
    temp2_list.append(float(var[2]))
# or #
    time = int(var[0])
    temp1 = float(var[1])
    temp2 = float(var[1])

    time_list.append(time)
    temp1_list.append(temp1)
    temp2_list.append(temp2)
'''
#printing the data to the terminal
print(time_list, '\n')
print(temp1_list, '\n')
print(temp2_list)