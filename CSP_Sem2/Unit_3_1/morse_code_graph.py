# # # # # # # # # #
import matplotlib.pyplot as plt

path = 'data_files/morse_graph.csv'

with open(path) as f:
    data = f.read().split('\n')

# # #
time_list = []
data4_list = []
data6_list = []
data9_list = []
data12_list = []
data13_list = []
data14_list = []

# # #
for line in data[1:]:
	split_line = line.split(',')
	# # #
	for line in data:
		time_list.append(float(split_line[0]))
		data4_list.append(float(split_line[1]))
		data6_list.append(float(split_line[2]))
		data9_list.append(float(split_line[3]))
		data12_list.append(float(split_line[4]))
		data13_list.append(float(split_line[5]))
		data14_list.append(float(split_line[6]))

# # #
plt.grid(b=None, which='major', axis='both')
plt.grid(color='grey')

plt.plot(time_list, data4_list, c='red')
plt.plot(time_list, data6_list, c='orange')
plt.plot(time_list, data9_list, c='yellow')
plt.plot(time_list, data12_list, c='green')
plt.plot(time_list, data13_list, c='blue')
plt.plot(time_list, data14_list, c='purple')

plt.title('3.1.1 Unknown Substance ')
plt.xlabel('Time (Seconds)')
plt.ylabel('Tempurature (Celcius)')

# # #
plt.show()
# # # # # # # # # #