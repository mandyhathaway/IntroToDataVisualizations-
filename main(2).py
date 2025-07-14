import matplotlib.pyplot as plt
import pandas as pd  

data = pd.read_csv('LifeData.csv')

data2=pd.read_csv('Medical_doctors.csv') 

##Pull out the data 

Afgh_death_data = data[data['Country'] == 'Afghanistan'][['Year', 'AdultMortality(women)']]
Peru_death_data = data[data['Country'] == 'Peru'][['Year', 'AdultMortality(women)']]

Afgh_med_docs_data = data2[data2['Country'] == 'Afghanistan'][['Year', 'Medicaldoctors(per10000population)']]
Peru_med_docs_data= data2[data2['Country'] == 'Peru'][['Year', 'Medicaldoctors(per10000population)']]

# Merge the datasets on 'Year' for comparison
                                                              
Afgh_combined_data = pd.merge(Afgh_death_data, Afgh_med_docs_data, on='Year')
Peru_combined_data = pd.merge(Peru_death_data, Peru_med_docs_data, on='Year')


# Plotting the data for comparison
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting Afghanistan data
ax.bar(Afgh_combined_data['Year'] - 0.2, Afgh_combined_data['AdultMortality(women)'], width=0.4, label='Afghanistan Mortality', align='center')
ax.bar(Afgh_combined_data['Year'] - 0.2, Afgh_combined_data['Medicaldoctors(per10000population)'], width=0.4, bottom=Afgh_combined_data['AdultMortality(women)'], label='Afghanistan Doctors', align='center')

# Plotting Peru data
ax.bar(Peru_combined_data['Year'] + 0.2, Peru_combined_data['AdultMortality(women)'], width=0.4, label='Peru Mortality', align='center')
ax.bar(Peru_combined_data['Year'] + 0.2, Peru_combined_data['Medicaldoctors(per10000population)'], width=0.4, bottom=Peru_combined_data['AdultMortality(women)'], label='Peru Doctors', align='center')

ax.set_ylabel('Counts')
ax.set_title('Comparison of Adult Mortality and Medical Doctors per 10,000 Population')
ax.legend()
plt.xticks(Afgh_combined_data['Year'])
plt.show()