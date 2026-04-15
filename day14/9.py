import numpy as np
import pandas as pd

arr = np.array([10, np.nan, 30, np.nan, 50])

S = pd.Series(arr)

mean_value = S.mean()

S = S.fillna(mean_value)

print(S)
