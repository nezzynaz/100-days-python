'''Exploring accessing CSV with Python'''

# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html

import csv # The csv package allows you to manipulate CSV files and makes working with it easier.

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)