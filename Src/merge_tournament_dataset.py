import pandas as pd

# Load Elo dataset
elo_df = pd.read_csv(
    "Data/Processed/ml_dataset_elo.csv"
)

# Load tournament features
tournament_df = pd.read_csv(
    "Data/Processed/tournament_features.csv"
)

# Merge side-by-side
final_df = pd.concat(
    [elo_df, tournament_df],
    axis=1
)

# Save final dataset
final_df.to_csv(
    "Data/Processed/ml_dataset_elo_tournament.csv",
    index=False
)

print("\nDataset merged successfully!")

print("\nShape:")
print(final_df.shape)

print("\nColumns:")
print(final_df.columns.tolist())

print("\nFirst 5 Rows:")
print(final_df.head())