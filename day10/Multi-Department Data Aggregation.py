import numpy as np

branchA = np.array([[10, 20],
                    [30, 40]])

branchB = np.array([[5, 15],
                    [25, 35]])

combined = branchA + branchB

total_employees = np.sum(combined)

print("Combined Employee Matrix:")
print(combined)
print("Total Employees:", total_employees)