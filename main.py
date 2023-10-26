import csv
import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# print(data["temp"].max())
# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)
data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [len(data[data["Primary Fur Color"] == "Gray"]), len(data[data["Primary Fur Color"] == "Cinnamon"]),
            len(data[data["Primary Fur Color"] == "Black"])]
  }
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")