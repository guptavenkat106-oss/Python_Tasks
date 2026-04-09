import numpy as np

prices_list = [499, 299, 799, 199, 599]

prices_array = np.array(prices_list)

sorted_prices = np.sort(prices_array)

print("Sorted Prices:", sorted_prices)