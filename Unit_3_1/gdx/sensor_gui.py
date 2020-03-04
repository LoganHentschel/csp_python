from tkinter import *
import gdx, time
import matplotlib.pyplot as plt

root = Tk()
gdx = gdx.gdx()

# # # # # #
def start_sensing():
    measurements_list = []
    A_sensor_list = [] #0
    C_sensor_list = [] #1
    time_list = []
    time = 0
    #
    seconds = int(seconds_entry.get())
    samples = int(samples_entry.get())
    period = 1000 // samples
    #
    gdx.open_usb()
    gdx.select_sensors([2,3])
    gdx.start(period=period)
    # #
    for i in range(seconds*samples):
        measurements = gdx.read()
        if measurements == None: 
            break 
        print(measurements)
        measurements_list.append(measurements)
    # #
    for line in measurements_list:
        A_sensor_list.append(line[0])
        C_sensor_list.append(line[1])
        time_list.append(time)
        time += 1/samples
    
    plt.plot(time_list, A_sensor_list, c='skyblue')
    plt.plot(time_list, C_sensor_list, c='lightgreen')

    plt.show()

# # # #
seconds_label = Label(root, text="How many seconds should the sensor run?")
seconds_label.pack()

seconds_entry = Entry(root)
seconds_entry.pack()

samples_label = Label(root, text="How many samples should the sensor take per second?")
samples_label.pack()

samples_entry = Entry(root)
samples_entry.pack()

start_button = Button(root, text="Start Sensing", command=start_sensing)
start_button.pack()

# # #
plt.grid(b=None, which='major', axis='both')

plt.title('Sensor Graphing ')
plt.xlabel('Time (Seconds)')
plt.ylabel('amu or something idk')

# # # # # #
root.mainloop()
gdx.stop()
gdx.close()
#plt.show()