import numpy as np

temperatures = np.array([
    [30, 32, 31],
    [29, 33, 34]
])

print("Temperature Array:")
print(temperatures)

total_temp = np.sum(temperatures)
print("Total Temperature Recorded:", total_temp)