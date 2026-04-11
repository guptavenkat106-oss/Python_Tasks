data = [[1, 2, 3], [4, 5], [6]]

flat = [num for sublist in data for num in sublist]

print(flat)
