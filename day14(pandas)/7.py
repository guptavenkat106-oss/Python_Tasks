import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

result = S1 + S2
print("Initial addition:")
print(result)

final_result = S1.add(S2, fill_value=0)
print("\nAfter replacing NaN with 0:")
print(final_result)

print("\nExplanation:")
print("NaN appears because pandas aligns data by index labels.")
print("If a label exists in one Series but not the other, the result is NaN.")
