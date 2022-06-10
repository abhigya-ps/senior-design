import numpy as np

data = [80, 60, 65, 70, 73, 82, 55, 62, 38, 40, 75, 68]
print("Previous temperatures:\n", sorted(data))

# ask user to enter a temperature value
temp = float(input("\nEnter a temperature value: "))

# check if this value is within the inter-quartile range
q1 = np.percentile(data, 25)
median = np.percentile(data, 50)
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("\nQuartile 1:", q1)
print("Median:", median)
print("Quartile 3:", q3)
print("Inter-Quartile Range:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

if temp < lower_bound or temp > upper_bound:
    print("\nThis temperature is an outlier.")
else:
    print("\nThis temperature is within bounds.")
