import pandas as pd
import numpy as np

df = pd.read_csv('AQI_Data.csv')
print("First 5 rows of the data set")
print(df.head(5))

print(df.tail(6))

Ques_stats = df.describe()
print("\nLast 6 rows of the data set")
print(Ques_stats)

columns = df[['City', 'AQI', 'PM2.5', 'PM10']]
grouped = columns.groupby('City')
Answer = grouped.mean()

print(Answer)

Question_data = df[df['PM2.5'] > 100]
city_counts = {}
for city in Question_data['City']:
    if city in city_counts:
        city_counts[city] += 1
    else: 
        city_counts[city] = 1

city_counts
print(city_counts)

