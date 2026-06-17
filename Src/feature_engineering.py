import pandas as pd

df = pd.read_csv(
    "Data/Raw/results.csv",
    encoding="latin1"
)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


def get_team_form(team, current_date):

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
    goals_scored = 0
    goals_conceded = 0

    for _, match in matches.iterrows():

        if match["home_team"] == team:

            goals_scored += match["home_score"]
            goals_conceded += match["away_score"]

            if match["home_score"] > match["away_score"]:
                wins += 1

        else:

            goals_scored += match["away_score"]
            goals_conceded += match["home_score"]

            if match["away_score"] > match["home_score"]:
                wins += 1

    return {
        "wins_last5": wins,
        "goals_scored_last5": goals_scored,
        "goals_conceded_last5": goals_conceded
    }


sample_match = df.iloc[10000]

home_team = sample_match["home_team"]

form = get_team_form(
    home_team,
    sample_match["date"]
)

print("Team:", home_team)
print(form)