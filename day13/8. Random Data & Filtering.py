import numpy as np

nums = np.random.randint(1, 100, 10)

filtered = nums[nums % 5 == 0]
result = np.sort(filtered)

print("Generated numbers:", nums)
print("Filtered & sorted (divisible by 5):", result)
