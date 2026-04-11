import numpy as np

data = [50, 60, 70, 80, 90, 100, 110, 120]

arr = np.array(data)

parts = np.array_split(arr, 4)

for i, part in enumerate(parts):
    print(f"Server {i+1}:", part)