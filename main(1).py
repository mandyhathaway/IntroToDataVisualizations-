import pandas as pd
from matplotlib import pyplot as plt
##Read the data from CSV files

raw_data = pd.read_csv("global_covid19_data.csv")
Us_data = raw_data[raw_data["location"]== "United States"]
#Antigua_data = raw_data[raw_data["location"]== "Antigua and Barbuda"] 
#Haiti_data = raw_data[raw_data["location"]== "Haiti"]
#Cuba_data = raw_data[raw_data["location"]== "Cuba"]
#Verde_data = raw_data[raw_data["location"]== "Cape Verde"]
Japan_data = raw_data[raw_data["location"]== "Japan"]


#y1= Antigua_data['people_fully_vaccinated_per_hundred']
#z1 = Haiti_data['people_fully_vaccinated_per_hundred']
#a1 = Cuba_data['people_fully_vaccinated_per_hundred']
#b1 = Verde_data['people_fully_vaccinated_per_hundred']
#c1 = Japan_data['people_fully_vaccinated_per_hundred']
#d1 = Us_data['people_fully_vaccinated_per_hundred']

#I1 = Antigua_data["icu_patients"]
#I2 = Haiti_data["icu_patients"]
#I3 = Cuba_data["icu_patients"]
#I4 = Verde_data["icu_patients"]
#I5 = Japan_data["icu_patients"]
#I6 = Us_data["icu_patients"]


### set up visualizations ----------------------------------------------------------------------

## #1  print size of database -------------
#print()
#print(raw_data.shape)


##  #2 single country look, deaths and new cases ------------------
plt.plot(Us_data.date, Us_data.total_deaths, color='red')
plt.plot(Japan_data.date, Japan_data.total_deaths, color='black')



# Format X axis label
plt.xticks([60, 120, 180, 240, 300, 360, 420,480, 520])

plt.xlabel("Dates (every 2 months)")
plt.xticks(rotation=20)
plt.ylabel("Numbers")
plt.title("Deaths Japan vs Haiti Covid19 (Mar 2020 to June 2021)")
plt.legend(['Total Deaths'])
plt.show()

#### #3 cross country comparison---------------------
#x_values = ["Cuba","Antigua","Haiti", "Japan"]
#y_values = [a1.iloc[0], y1.iloc[0], z1.iloc[0], c1.iloc[0]]
#plt.barh(x_values,y_values, color ="yellowgreen")
#plt.xlabel("People Immunized Per 100")
#plt.ylabel("Countries")
#plt.title("Country Comparison - Immunization level")
#plt.show()