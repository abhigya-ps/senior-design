# mean
def mean(data):
    n = len(data)
    total = 0
    for d in data:
        total += d
    mean = total / n
    return mean

# standard deviation
def standard_deviation(data):
    n = len(data)
    differences = [0] * n   # [0, 0, 0, 0, 0]

    for i in range(n): 
        diff = data[i] - mean(data)
        differences[i] = round(diff, 2)

    # squaring the differences
    for i in range(n):
        differences[i] = differences[i]**2

    # adding the differences
    total = 0
    for diff in differences:
        total += diff

    variance = total / (n - 1)
    sd = round(variance ** (1/2), 2)
    return sd

# quartiles
def quartile(percent, data):
    n = len(data)
    data = sorted(data)
    index = (percent / 100) * (n + 1) - 1
    if index != floor(index):   # index is a decimal
        i = floor(index)
        result = (data[i] + data[i + 1]) / 2
    else:
        result = data[index - 1]
    
    return result

