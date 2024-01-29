# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # set Data in columns
# print(data["condition"])
# print(data.condition)

# set data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(monday_temp)
#
# data_dict = {
#     "students": ["Amy", "Majorie", "Juliana"],
#     "scores": [75, 82, 89]
# }
#
# one_data = pandas.DataFrame(data_dict)
# one_data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(cinnamon_squirrels)
print(black_squirrels)
print(gray_squirrels)
