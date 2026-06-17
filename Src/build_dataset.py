import pandas as pd

df = pd.read_csv(
    "Data/Raw/results.csv",
    encoding="latin1"
)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


def team_form(team, current_date):

    matches = df[
        (
            (df["home_team"] == team)
            |
            (df["away_team"] == team)
        )
        &
        (df["date"] < current_date)
    ].tail(5)

    wins = 0
    scored = 0
    conceded = 0

    for _, match in matches.iterrows():

        if match["home_team"] == team:

            scored += match["home_score"]
            conceded += match["away_score"]

            if match["home_score"] > match["away_score"]:
                wins += 1

        else:

            scored += match["away_score"]
            conceded += match["home_score"]

            if match["away_score"] > match["home_score"]:
                wins += 1

    return wins, scored, conceded


rows = []

for index, match in df.iterrows():

    if index % 1000 == 0:
        print(index)

    hw, hgs, hgc = team_form(
        match["home_team"],
        match["date"]
    )

    aw, ags, agc = team_form(
        match["away_team"],
        match["date"]
    )

    if match["home_score"] > match["away_score"]:
        target = 2

    elif match["home_score"] < match["away_score"]:
        target = 0

    else:
        target = 1

    rows.append({
        "home_wins_last5": hw,
        "away_wins_last5": aw,
        "home_goals_scored_last5": hgs,
        "away_goals_scored_last5": ags,
        "home_goals_conceded_last5": hgc,
        "away_goals_conceded_last5": agc,
        "target": target
    })

ml_df = pd.DataFrame(rows)

ml_df.to_csv(
    "Data/Processed/ml_dataset.csv",
    index=False
)

print("DONE")
print(ml_df.head())