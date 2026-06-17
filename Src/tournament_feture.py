import pandas as pd

df = pd.read_csv(
    "Data/Raw/results.csv",
    encoding="latin1"
)

def tournament_category(name):

    name = str(name).lower()

    if "friendly" in name:
        return 0

    elif "world cup" in name and "qualification" not in name:
        return 1

    elif "world cup qualification" in name:
        return 2

    elif (
        "euro" in name
        or "copa" in name
        or "asian cup" in name
        or "african cup" in name
        or "gold cup" in name
        or "nations league" in name
    ) and "qualification" not in name:
        return 3

    elif "qualification" in name:
        return 4

    else:
        return 5


df["tournament_category"] = df["tournament"].apply(
    tournament_category
)

feature_df = df[["tournament_category"]]

feature_df.to_csv(
    "Data/Processed/tournament_features.csv",
    index=False
)

print(feature_df.head())
print(feature_df["tournament_category"].value_counts())