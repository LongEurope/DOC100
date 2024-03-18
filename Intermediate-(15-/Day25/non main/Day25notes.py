#https://pandas.pydata.org/docs/reference/series.html

#Working with csv files and analysing data with pandas.

# Getting the temperatures and converting them to integer and appending to list, without pandas.
# with open(r'DOC100\Intermediate-(15-\Day25\weather_data.csv', mode='r') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Further working with pandas:
# data = pd.read_csv(r'DOC100\Intermediate-(15-\Day25\weather_data.csv')

# Converting the dataframe and series to different file types
# data_dict = data.to_dict()
# data_temp_list = data['temp'].to_list()

# print(data_dict)
# print(data_temp_list)


# Example of optimisation with methods from panda
# # temp_list = data['temp'].to_list()

# # average = round(sum(temp_list) / len(temp_list))

# # print(f'Average: {average} Degrees Celsius')

# print(round(data['temp'].mean()))

# Getting row with max temperature
#print(data[data['temp'] == data['temp'].max()])


#------------------------


# data = pd.read_csv(r'DOC100\Intermediate-(15-\Day25\weather_data.csv')

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday.temp = (monday.temp * 9/5) + 32

#Creating a dataframe

# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv('practice_data.csv')