import pandas as pd

data = pd.read_csv(r'DOC100\Intermediate-(15-\Day25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240318.csv')

grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')