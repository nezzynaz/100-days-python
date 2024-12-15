'''experimenting with pandas'''

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# The following can convert a pandas datatype and series into a dictionary and list

data_list = data["temp"].to_list()
data_dict = data.to_dict()

# This is how one could find the average of a set of data using built-in python functions
# However, there is an easier way to do it.
# average = sum(data_list) / len(data_list)
# print(average)

# This built-in function will find the mean as well. You can find the median and mode as well if you call it on a data series.
#print(data["temp"].mean())

# For instance, this will find the max.
# print(data["temp"].max())

# You can get data in columns by asking for the column (from the first row)
# print(data["condition"])
# alternatively..
# print(data.condition)
# both selections are viable, but ensure its case sensitive.

# To get a data in rows, you need to do a little more..
# print(data[data.day == "Monday"])

# daymax = data.temp.max() #notice how like above, you can just do data.temp instead of data["temp"]. Less strings to write.
#  print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_f = (monday_temp*1.8)+32
# print(monday_f)

# This is how you create a dataframe from scratch, as well as make a CSV from the data.
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

newdata = pandas.DataFrame(data_dict)
newdata.to_csv("new_data.csv")
