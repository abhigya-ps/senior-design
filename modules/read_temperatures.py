import pandas as pd
import numpy as np

filename = "temperatures.csv"
df = pd.read_csv(filename)
times = df["Time"]             # list of timestamps

# print(type(list(times)[0]))
# for i in range(len(times)):
#     print(times[i])

last_Mon = df["Mon 06/06"]      # temperatures from last Monday
this_Mon = df["Mon 06/13"]      # temperatures from this week's Monday
print("Temperatures from last Mon 06/06:\n", list(last_Mon))

# find the median
median = np.percentile(last_Mon, 50)

# find the standard deviation
sd = np.std(last_Mon)

# if the user's temperature is beyond 2 sd's, it is an outlier
lower_bound = median - 2 * sd
upper_bound = median + 2 * sd

print("\nMedian:", median)
print("Standard Deviation:", round(sd, 2))
print("Lower Bound:", round(lower_bound, 2))
print("Upper Bound:", round(upper_bound, 2))

for i in range(len(times)):
    time = times[i]
    temp = this_Mon[i]
    print(f"Time: {time}, Temp: {temp}")
        
    if temp < lower_bound or temp > upper_bound:
        print("Temperature is an outlier.\n")
    else:
        print("Temperature is within bounds.\n")
