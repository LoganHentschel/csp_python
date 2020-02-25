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
		time_list.append(float(split_line[0]))
		data_615nm_list.append(float(split_line[1]))
		data_525nm_list.append(float(split_line[2]))
		data_465nm_list.append(float(split_line[3]))

# # #
f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharey=True)
f.tight_layout(pad=3)

ax1.plot(time_list, data_615nm_list, c='red')
ax1.set_title('615 nm')
ax1.set(ylabel='Nanometers')
#
ax2.plot(time_list, data_525nm_list, c='blue')
ax2.set_title('525 nm')
ax2.set(ylabel='Nanometers')
#
ax3.plot(time_list, data_465nm_list, c='green')
ax3.set_title('465 nm')
ax3.set(ylabel='Nanometers')
# #
plt.xlabel('Time (Seconds)')


# # #
plt.show()