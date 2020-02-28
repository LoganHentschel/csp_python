# Ask user how long they want to collect data
# Ask how many samples they want per second
# -Collect for that long

# Show a graph of the data

import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors([2,3])
gdx.start(period=1000) #1000 milliseconds = 1 second, period is amount of time between readings

for i in range(0,5):
    measurements = gdx.read() #returns a list of measurements from the sensors selected.
    if measurements == None: 
        break 
    print(measurements)

gdx.stop()
gdx.close()

