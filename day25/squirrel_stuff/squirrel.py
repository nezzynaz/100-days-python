'''Experimenting with Pandas and a large dataset'''

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
# Once we access the rows, it gets treated like an iterable (a list), which lets us use len() on this.
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

# This was my attempt at the project trying to access the data through the nunique() function
# instead. I thought this idea was better because you may not always have three colors to base
# your findings on, and this would allow for a lot more flexibility if the dataset was larger
# in terms of fur color.

# fur_count = data.groupby("Primary Fur Color")["Hectare Squirrel Number"].nunique()
# print(fur_count)
# fur_count.rename(columns={"Primary Fur Color": "Fur Color", "Hectare Squirrel Number": "Count"})
# new_squirrel = pandas.DataFrame(fur_count)
