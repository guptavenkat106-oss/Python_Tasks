import numpy as np

sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

avg = np.mean(sales)
filtered_sales = sales[sales > avg]

print(filtered_sales)
