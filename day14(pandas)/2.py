import pandas as pd

cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}

S = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

missing = S.isna()

print(S)
print("\nMissing values:")
print(missing)
