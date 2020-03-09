'''CSP ASSIGNMENT
6 graphs: 3 coulombs 2 rows
Weather-y title on top

Actual mean - actual min - actual max 
Actual precipitation - record min temp - record max'''
# # # # # # #
import matplotlib.pyplot as plt

path = 'data_files/weather.csv'

with open(path) as f:
    data = f.read().split('\n')

# # #
date_list = [] #0
actual_mean_temp = [] #1
actual_min_temp = [] #2
actual_max_temp = [] #3
record_min_temp = [] #6
record_max_temp = [] #7
actual_precipitation = [] #10


# # #
for n, line in enumerate(data[1:]):
    split_line = line.split(',')
    for variable in split_line:
        date_list.append(n)
        actual_mean_temp.append(float(split_line[1]))
        actual_min_temp.append(float(split_line[2]))
        actual_max_temp.append(float(split_line[3]))
        record_min_temp.append(float(split_line[6]))
        record_max_temp.append(float(split_line[7]))
        actual_precipitation.append(float(split_line[10]))
# # # #
fig, ax1 = plt.subplots(2, 3)
fig.tight_layout(pad=3)

ax1[0][0].plot(date_list, actual_mean_temp, c='green')
ax1[0][0].set_title('Actual Mean Temp')

ax1[0][1].plot(date_list, actual_min_temp, c='skyblue')
ax1[0][1].set_title('Actual Min Temp')

ax1[0][2].plot(date_list, actual_max_temp, c='red')
ax1[0][2].set_title('Actual Max Temp')

ax1[1][1].plot(date_list, record_min_temp, c='purple')
ax1[1][1].set_title('Record Min Temp')

ax1[1][2].plot(date_list, record_max_temp, c='orange')
ax1[1][2].set_title('Record Max Temp')

ax1[1][0].plot(date_list, actual_precipitation, c='blue')
ax1[1][0].set_title('Actual Precipitation')

# # # #
plt.show()
# # # # # # #