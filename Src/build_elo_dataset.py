import pandas as pd

K = 20

df = pd.read_csv(
    "Data/Raw/results.csv",
    encoding="latin1"
)

ratings = {}

elo_rows = []

for _, row in df.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    home_elo = ratings.get(home, 1500)
    away_elo = ratings.get(away, 1500)

    elo_rows.append({
        "home_elo": home_elo,
        "away_elo": away_elo,
        "elo_difference": home_elo - away_elo
    })

    expected_home = 1 / (
        1 + 10 ** ((away_elo - home_elo) / 400)
    )

    if row["home_score"] > row["away_score"]:
        actual_home = 1

    elif row["home_score"] < row["away_score"]:
        actual_home = 0

    else:
        actual_home = 0.5

    ratings[home] = (
        home_elo
        + K * (actual_home - expected_home)
    )

    ratings[away] = (
        away_elo
        + K * (
            (1 - actual_home)
            - (1 - expected_home)
        )
    )

elo_df = pd.DataFrame(elo_rows)

elo_df.to_csv(
    "Data/Processed/elo_features.csv",
    index=False
)

print(elo_df.head())
print("\nShape:", elo_df.shape)