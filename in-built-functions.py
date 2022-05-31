import numpy as np

# mean
mean = np.mean(data)

# standard deviation
standard_deviation = np.std(data)

# percentiles or quartiles
median = np.percentile(data, 50)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

# Inter-quartile range and outlier detection
iqr = q3 - q1

# numbers outside this range are outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr



