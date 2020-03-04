
import gdx, time
import matplotlib.pyplot as plt

gdx = gdx.gdx()
# # #
seconds = int(input("How many seconds do you want to take samples for?"))
samples = int(input("How many samples do you want per second?"))
period = 1000 / samples

gdx.open_usb()
gdx.select_sensors([2,3])
gdx.start(period=period)


# # #
for i in range(0,5):
    measurements = gdx.read()
    if measurements == None: 
        break 
    print(measurements)

# # #
#for _ in range(time):
    #

# # # # #
gdx.stop()
gdx.close()

