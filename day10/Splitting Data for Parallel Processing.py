import numpy as np

data = np.array([5, 10, 15, 20, 25, 30])

split_data = np.array_split(data, 3)

print("Split Data:")
for i, part in enumerate(split_data, 1):
    print(f"Part {i}:", part)