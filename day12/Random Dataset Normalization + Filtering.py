import numpy as np

data = np.random.rand(8)

print("Original data:", data)

normalized = data * 100
print("Normalized data:", normalized)

filtered = normalized[normalized > 50]

print("Filtered (>50):", filtered)

sorted_values = np.sort(filtered)

print("Sorted filtered values:", sorted_values)
