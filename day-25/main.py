# Just simply open the file
# with open("weather_data.csv", mode='r') as data_file:
#     data = data_file.readlines()
#     print(data)
#
# # Using CSV
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#     print(temperatures)

# import pandas

# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)

# Get Data in Rows
# print(data[data['day'] == 'Monday'])
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)
# monday_temp_on_fahrenheit = monday.temp * 1.8 + 32
# print(monday_temp_on_fahrenheit)

# Create a DataFrame from scratch
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


# # My version
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# colors = data['Primary Fur Color'].unique().tolist()
#
# counts = []
# for color in colors[1:]:
#     squirrels_color = data[data['Primary Fur Color'] == color]
#     squirrels_count = squirrels_color['Primary Fur Color'].count()
#     counts.append(squirrels_count)
#
# data_dict = {
#     "Fur Color": colors[1:],
#     "Count": counts,
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")

# Angela's solution
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
# red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
# black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
