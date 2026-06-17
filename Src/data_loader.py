import pandas as pd

df = pd.read_csv(
    "Data/Raw/results.csv",
    encoding="latin1"
)

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset Shape:")
print(df.shape)