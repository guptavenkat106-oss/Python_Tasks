import numpy as np

arr = np.array([10, 20, 30, 40])

arr_copy = arr.copy()

arr[0] = 99

print("Original array:", arr)
print("Copy array:", arr_copy)

arr_view = arr.view()

arr[1] = 77

print("Original array after second change:", arr)
print("View array:", arr_view)