import pandas as pd

S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])

S_total = S1 + S2
total_sales = S_total.sum()

print(S_total)
print("Total sales:", total_sales)
