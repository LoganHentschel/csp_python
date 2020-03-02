
import gdx, time
import matplotlib.pyplot as plt
# # # # #
gdx = gdx.gdx()

# # #
gdx.open_usb()

seconds = int(input("How many seconds do you want to take samples for?"))
samples = int(input("How many samples do you want per second?"))
period = 1000 / samples


gdx.select_sensors([2,3])
gdx.start(period=period)
#print('--- Please select time frame for data collection in miliseconds below --- \n 1000 miliseconds = 1 second')
#time = input('Please input the amount of samples wanted per second: ')

# # #
for i in range(0,5):
    measurements = gdx.read() #returns a list of measurements from the sensors selected.
    if measurements == None: 
        break 
    print(measurements)

# # #
#for _ in range(time):
    #

# # # # #
gdx.stop()
gdx.close()

