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

        #basic stats:
    print(data.describe)
    print("Average cases in 2020 (/day): \n" , round(np.mean(data['cases']), 3))
    print("Average deaths in 2020 (/day): \n" , round(np.mean(data['deaths']), 3))
    print("Highest cases: ")
    print(data[data.cases == data.cases.max()].cases)
    print("Caseless days: ")
    print(data[['cases', 'deaths']][data.cases == data['cases'].min()])


def main():
    covid_data = pd.read_csv("ca-covid.csv")
    analize_data(covid_data)

main()