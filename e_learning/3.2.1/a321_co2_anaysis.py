import matplotlib.pyplot as plt
import pandas as pd
import math
# # # # # 
co2_data = pd.read_csv("co2_data.csv", header=0)   

print(co2_data) #1 PRINT

co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data) #2 PRINT

co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data) #3 PRINT

# # #
#x decimal year, y average value
plt.ylabel('CO2 Averages') 
plt.xlabel('Decimal Year') #unique for each row
plt.title('Co2 Analysis')

# # # 
#x,y
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='gray')
plt.show()

