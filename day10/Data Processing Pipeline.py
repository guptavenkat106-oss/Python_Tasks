import numpy as np

data_list = [12, 7, 25, 3, 18, 10]
data_array = np.array(data_list)

sorted_array = np.sort(data_array)

split_arrays = np.array_split(sorted_array, 2)
part1, part2 = split_arrays[0], split_arrays[1]

sum_part1 = np.sum(part1)
sum_part2 = np.sum(part2)

print("Sorted Array:", sorted_array)
print("Part 1:", part1)
print("Part 2:", part2)
print("Sum of Part 1:", sum_part1)
print("Sum of Part 2:", sum_part2)