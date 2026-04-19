import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

series = pd.Series(data)

mean_value = series.mean()
cleaned_series = series.fillna(mean_value)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(cleaned_series, marker='o')
plt.title("Cleaned Data - Line Graph")
plt.xlabel("Index")
plt.ylabel("Values")

average = cleaned_series.mean()
filtered = cleaned_series[cleaned_series > average]

plt.subplot(1, 2, 2)
plt.bar(filtered.index.astype(str), filtered.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")

plt.tight_layout()
plt.show()
