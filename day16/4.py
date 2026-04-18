import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

temp_series = pd.Series(temps)

plt.plot(temp_series, marker='o')

plt.title("Daily Temperature Trend")
plt.grid(True)

plt.show()
