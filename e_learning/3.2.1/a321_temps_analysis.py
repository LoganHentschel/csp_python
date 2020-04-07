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
#plt.show()

## matplotlib is used to make the bar chart
plt.bar(temp_data['Year'], temp_data['Anomaly'], align='center', color='green')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

#Calculates min, max, and avg anomaly and the corresponding min/max years
min_anomaly = temp_data['Anomaly'][0]
max_anomaly = temp_data['Anomaly'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0

for i in range(0, len(temp_data['Anomaly'])):
  if (temp_data['Anomaly'][i] < min_anomaly):
    min_anomaly = temp_data['Anomaly'][i]
    min_year = temp_data['Year'][i]
  if (temp_data['Anomaly'][i] > max_anomaly):
    max_anomaly = temp_data['Anomaly'][i]
    max_year = temp_data['Year'][i]
  sum_anomaly = sum_anomaly + temp_data['Anomaly'][i]

# calculate average
avg_anomaly = sum_anomaly/len(temp_data['Anomaly'])

# print the statistical values
print("The maximum anomaly is:", max_anomaly, "which occured in", max_year)
print("The minimum anomaly is:", min_anomaly, "which occured in", min_year)
print("The average anomaly is:", avg_anomaly)

# # # # #