import matplotlib.pyplot as plt
import pandas as pd  

# Reading CSV files
data = pd.read_csv('LifeData.csv')
data2 = pd.read_csv('cross-country-literacy-rates.csv')

# Pulling out the data
# Ukraine
Ukr_life_data = data[(data['Country'] == 'Ukraine') & (data['Year'].between(2006, 2015))][['Year', 'Lifeexpectancy(women)']]
Ukr_lit_data = data2[(data2['Country'] == 'Ukraine') & (data2['Year'].between(2006, 2015))][['Year', 'Historical']]
Ukr_combined_data = pd.merge(Ukr_lit_data, Ukr_life_data, on='Year')


# Turkey
Tur_life_data = data[(data['Country'] == 'Turkey') & (data['Year'].between(2006, 2015))][['Year', 'Lifeexpectancy(women)']]
Tur_lit_data = data2[(data2['Country'] == 'Turkey') & (data2['Year'].between(2006, 2015))][['Year', 'Historical']]
Tur_combined_data = pd.merge(Tur_lit_data, Tur_life_data, on='Year')

# VEN
VEN_life_data = data[(data['Country'] == 'Venezuela (Bolivarian Republic of)') & (data['Year'].between(2006, 2015))][['Year', 'Lifeexpectancy(women)']]
VEN_lit_data = data2[(data2['Country'] == 'Venezuela') & (data2['Year'].between(2006, 2015))][['Year', 'Historical']]
VEN_combined_data = pd.merge(VEN_lit_data, VEN_life_data, on='Year')

# Print statements for debugging
print("VEN Life Data:")
print(VEN_life_data)
print("VEN Literacy Data:")
print(VEN_lit_data)
print("VEN Combined Data:")
print(VEN_combined_data)

# Plotting the data for comparison
fig, ax = plt.subplots(figsize=(10, 10))

# Corrected Ukraine plotting commands
ax.bar(Ukr_combined_data['Year'] - 0.2, Ukr_combined_data['Historical'], width=0.4, label='Ukr Literacy Rate', align='center', color = 'blue')
ax.bar(Ukr_combined_data['Year'] + 0.2, Ukr_combined_data['Lifeexpectancy(women)'], width=0.4, label='Ukr Mortality Rate', align='center', color = 'orange')

# Corrected VEN plotting commands: using merged VEN data
ax.bar(VEN_combined_data['Year'] - 0.2, VEN_combined_data['Historical'], width=0.4, label='VEN Literacy Rate', align='center', color = 'purple')
ax.bar(VEN_combined_data['Year'] + 0.2, VEN_combined_data['Lifeexpectancy(women)'], width=0.4, label='VEN Mortality Rate', align='center', color = 'yellow')

# Corrected Turkey plotting commands
ax.bar(Tur_combined_data['Year'] - 0.2, Tur_combined_data['Historical'], width=0.4, label='Tur Literacy Rate', align='center', color = 'green')
ax.bar(Tur_combined_data['Year'] + 0.2, Tur_combined_data['Lifeexpectancy(women)'], width=0.4, label='Tur Mortality Rate', align='center', color = 'red')



ax.set_ylabel('Counts')
ax.set_title('Comparison of Women Mortality and Literacy rate')
ax.legend()

# Corrected use of the variable name for xticks
plt.xticks(list(Ukr_combined_data['Year'].unique()) + list(Tur_combined_data['Year'].unique()) + list(VEN_combined_data['Year'].unique()))  # Shows all unique years
plt.show()