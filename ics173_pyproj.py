# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filepath = r"C:\Users\drswa\OneDrive\Documents\COLLEGE - UHMC 22-24\2022 FALL\ICS 173\data sets for final proj\Aquaponics.csv"
#use r"c:\filepath" to read
aqua_data = pd.read_csv(filepath)

print(aqua_data.head())
#print(aqua_data.describe())

#parse dates for date column
from datetime import datetime, timezone
aqua_data['Date:'] = pd.to_datetime(aqua_data['Date:'], format='%m/%d/%Y')
#aqua_data.info()

#find useful columns, set new data frame

aqua_df = pd.DataFrame(aqua_data, columns=['pH','Dissolved Oxygen','Date:'])
#print(aqua_df.head())
#print('pH data type: ',aqua_df['pH'].dtype)
#print('Dissolved Oxygen data type: ',aqua_df['Dissolved Oxygen'].dtype)
#print('Date: ', aqua_df['Date:'].dtype)

#comparitive scatterplot with line
aqua_df.plot(x="Date:", y="pH", style=":", figsize=(12, 8), color='r')
plt.xlabel('Date (Year-Month-Day)')
plt.ylabel('pH Level')
plt.show()
#convert column to float
phmean = np.mean(aqua_df['pH'])
domean = np.mean(aqua_df['Dissolved Oxygen'])
print('pH mean: ', phmean,
      '\nDissolved Oxygen mean: ', domean)

sns.regplot(aqua_df['Dissolved Oxygen'], aqua_df['pH'], line_kws={'color':'green'})
#graph useful columns in the data frame
temp_df = pd.DataFrame(aqua_data, columns=['Water Temp','Room Temp'])
#temp_df = temp_df['Water Temp'].str.replace(",", ".").astype('float')
#temp_df = temp_df.astype({'Water Temp':'float'})# "Room Temp":'float'})
#temp_df.info()
sns.regplot(temp_df['Room Temp'], temp_df['Water Temp'].str.replace(",", ".").astype('float'), line_kws={'color':'blue'})

#set elements of graph



