## The pandas and matplotlib modules are used to create a graph of the data
## -- pandas loads the data sheets into it's own DataFrame objects
## -- whole matplotlib plots the graph and bar chart
import matplotlib.pyplot as plt
import pandas as pd

## Loads in the data with read_csv(), identifying the header row
temp_data = pd.read_csv("temperature_data.csv", header=0)   

## matplotlib is used to make the line graph
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')

## Plots Anomaly and LOWESS on the line graph
plt.plot(temp_data['Year'], temp_data['Anomaly'], color='gray')
plt.plot(temp_data['Year'], temp_data['LOWESS'], color='blue')

# TODO #4: Use matplotlib to make a bar chart


# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years

# # #
plt.show()