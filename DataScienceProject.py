import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

def analize_data(data):
        #original data:
    #print("original dataFrame:")
    #print(data)

        #cast date to date format:
    data['date'] = pd.to_datetime(data['date'], format = "%d.%m.%y")

        #set date to index:
    data.set_index(data['date'], inplace = True)

        #add weekdays, month and season:
    data['weekdays'] = data['date'].dt.strftime('%a')
    data['season'] = np.where((data['date'].dt.month >= 5)
                          & (data['date'].dt.month <= 9),
                         "Hot season", "Cool season")
    data['month'] = data['date'].dt.month_name()

        #delete unnecessary column:
    data.drop('state', axis = 1, inplace = True)

        #reorder cols:
    data = data[['season', 'month', 'weekdays', 'cases', 'deaths']]

        #basic stats:
    print(data.describe)
    print("Average cases in 2020 (/day): \n" , round(np.mean(data['cases']), 3))
    print("Average deaths in 2020 (/day): \n" , round(np.mean(data['deaths']), 3))
    print("Highest cases: ")
    print(data[data.cases == data.cases.max()].cases)
    print("Caseless days: ")
    print(data[['cases', 'deaths']][data.cases == data['cases'].min()])

        #diagram(line):
    data.groupby('date')[['cases', 'deaths']].sum().plot(kind = 'line')
    plt.show()

        #diagram(bar):
    data.groupby('season')['cases'].sum().plot(kind = 'barh', color = ['blue','red'])
        # after plotting the data, format the labels
    current_values = plt.gca().get_xticks()
        # using format string '{:,.0f}'
    plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in current_values])
    plt.show()

        #diagram(pie):
    data.groupby('weekdays')['deaths'].sum().plot(kind = 'pie')
    plt.show()

    weekends = data[['weekdays', 'cases', 'deaths']]
    wes = ['Fri', 'Sat', 'Sun']
    
    #weekdays diagram(bar):
    weekends["weekend"] = np.where((weekends["weekdays"] == 'Fri') | (weekends["weekdays"] == 'Sat') | (weekends["weekdays"] == 'Sun'),"Weekend", "Weekday")
    weekends.groupby('weekend')['deaths'].sum().plot(kind = 'bar')
    plt.show()

def main():
    covid_data = pd.read_csv("ca-covid.csv")
    analize_data(covid_data)

main()