import random
import csv
import pandas as pd

# generate timestamps for every 5 minutes, starting at 8am
timestamps = []

start_time = 800
sampling_rate = 1 / 5   # 1 sample recorded every 5 minutes
hours = 3  # 8am to 11am
no_of_samples = sampling_rate * (hours * 60)

time = start_time
for _ in range(int(no_of_samples)):
    timestamps.append(time)

    time += 5
    # move to the next hour after 60 minutes
    hour = (time // 100) * 100
    minute = time - hour
    if minute >= 60:
        time += 40

temperatures = []
for _ in range(8):  # 7 days a week + next Monday
    temperature = []
    for _ in range(len(timestamps)):
        temp = random.randint(40, 90)
        temperature.append(temp)
    temperatures.append(temperature)

data = []
for i in range(len(timestamps)):
    row = [timestamps[i]]
    for temp in temperatures:
        row.append(temp[i])
    data.append(row)
    
# convert to a dataframe
dates = ["Mon 06/06", "Tue 06/07", "Wed 06/08", "Thu 06/09", "Fri 06/10", "Sat 06/11", "Sun 06/12", "Mon 06/13"]
columns = ["Time"]
for date in dates:
    columns.append(date)
df = pd.DataFrame(data, columns = columns)

# save as a csv file
filename = "temperatures.csv"
df.to_csv(filename, index = False)



