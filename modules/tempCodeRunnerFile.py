
# median = np.percentile(last_Mon, 50)

# # find the standard deviation
# sd = np.std(last_Mon)

# # if the user's temperature is beyond 2 sd's, it is an outlier
# lower_bound = median - 2 * sd
# upper_bound = median + 2 * sd

# print("\nMedian:", median)
# print("Standard Deviation:", round(sd, 2))
# print("Lower Bound:", round(lower_bound, 2))
# print("Upper Bound:", round(upper_bound, 2))

# for temp in this_Mon
# if temp < lower_bound or temp > upper_bound:
#     print("\nThis temperature is an outlier.")
# else:
#     print("\nThis temperature is within bounds.")