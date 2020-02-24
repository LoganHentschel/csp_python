import matplotlib.pyplot as plt

path = 'data_files/light.csv'

with open(path) as f:
    data = f.read().split('\n')

# # # # #
time_list = []
data_615nm_list = []
data_525nm_list = []
data_465nm_list = []

# # #
for line in data[1:]:
	split_line = line.split(',')
	# # #
	for line in data:
		time_list.append(split_line[0])
		data_615nm_list.append(split_line[1])
		data_525nm_list.append(split_line[2])
		data_465nm_list.append(split_line[3])

# # #
plt.grid(b=None, which='major', axis='both')
#plt.grid(color='grey')

plt.plot(time_list, data_615nm_list, c='red')
plt.plot(time_list, data_525nm_list, c='green')
plt.plot(time_list, data_465nm_list, c='blue')

plt.title('Light Sensing')
plt.xlabel('Time (Seconds)')
plt.ylabel('light...?')

# # #
plt.show()


# # # # #
#fig, ax = pyplot.subplots(1,1)
#ax.plot([[1,2,3], [4,5,6]])
#pyplot.show()