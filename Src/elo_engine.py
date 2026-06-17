import pandas as pd

K = 20

def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

def update_elo(rating_a, rating_b, score_a):
    exp_a = expected_score(rating_a, rating_b)

    rating_a_new = rating_a + K * (score_a - exp_a)
    rating_b_new = rating_b + K * ((1 - score_a) - (1 - exp_a))

    return rating_a_new, rating_b_new


df = pd.read_csv("Data/Raw/results.csv", encoding="latin1")

ratings = {}

for team in pd.concat([df["home_team"], df["away_team"]]).unique():
    ratings[team] = 1500

for _, row in df.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    home_rating = ratings[home]
    away_rating = ratings[away]

    if row["home_score"] > row["away_score"]:
        score = 1

    elif row["home_score"] < row["away_score"]:
        score = 0

    else:
        score = 0.5

    new_home, new_away = update_elo(
        home_rating,
        away_rating,
        score
    )

    ratings[home] = new_home
    ratings[away] = new_away

print("Top 20 Teams\n")

top20 = sorted(
    ratings.items(),
    key=lambda x: x[1],
    reverse=True
)[:20]

for team, rating in top20:
    print(team, round(rating))