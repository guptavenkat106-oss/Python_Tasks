import numpy as np

temps = np.array([28, 31, 35, 27, 40, 22])

filtered = temps[temps > 30]

print(filtered)