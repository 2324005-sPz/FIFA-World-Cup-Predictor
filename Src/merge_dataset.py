import pandas as pd

ml_df = pd.read_csv(
    "Data/Processed/ml_dataset.csv"
)

elo_df = pd.read_csv(
    "Data/Processed/elo_features.csv"
)

final_df = pd.concat(
    [ml_df, elo_df],
    axis=1
)

final_df.to_csv(
    "Data/Processed/ml_dataset_elo.csv",
    index=False
)

print(final_df.head())
print("\nShape:", final_df.shape)
print("\nColumns:")
print(final_df.columns.tolist())