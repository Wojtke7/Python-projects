# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except ValueError:
#             continue
#
#     print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avr_temp = sum(temp_list) / len(temp_list)
# print(avr_temp)
#
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Creating dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("Squirrel_Data.csv")
color_list = data["Primary Fur Color"].to_list()
# print(color_list)

gray_color_count = color_list.count("Gray")
red_color_count = color_list.count("Cinnamon")
black_color_count = color_list.count("Black")

# print(gray_color_count)
# print(red_color_count)
# print(black_color_count)

colors_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_color_count, red_color_count, black_color_count]
}

data_frame = pandas.DataFrame(colors_dict)
data_frame.to_csv("colors_dict.csv")
