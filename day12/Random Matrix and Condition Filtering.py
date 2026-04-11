import numpy as np

matrix = np.random.randint(0, 51, (3, 3))

print("Matrix:")
print(matrix)

filtered = matrix[matrix > 25]

print("Values greater than 25:")
print(filtered)
