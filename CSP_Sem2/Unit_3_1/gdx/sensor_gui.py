from tkinter import *
import gdx, time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    # #
    ax.clear()
    #
    plt.title('Sensor Graphing ')
    plt.xlabel('Time (Seconds)')
    plt.ylabel('amu or something idk')
    #
    ax.plot(time_list, A_sensor_list, c='skyblue')
    ax.plot(time_list, C_sensor_list, c='lightgreen')
    

# # # #
seconds_label = Label(root, text="How many seconds should the sensor run?")
seconds_label.grid()

seconds_entry = Entry(root)
seconds_entry.grid()

samples_label = Label(root, text="How many samples should the sensor take per second?")
samples_label.grid()

samples_entry = Entry(root)
samples_entry.grid()

start_button = Button(root, text="Start Sensing", command=start_sensing)
start_button.grid()
 
# # #
gdx.open_usb()
gdx.select_sensors([2,3])

# # #
fig, ax = plt.subplots(1,1)
plt.ion()
chart = FigureCanvasTkAgg(fig,root)
chart.get_tk_widget().grid(column=1, row=0, rowspan=5 )

# # #
plt.title('Sensor Graphing ')
plt.xlabel('Time (Seconds)')
plt.ylabel('amu or something idk')

# # # # # #
root.mainloop()
gdx.stop()
gdx.close()
