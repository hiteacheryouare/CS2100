import pandas as bamboo

ALL_GAMES = "./all_games.csv"
df = bamboo.read_csv(ALL_GAMES, encoding="utf-8")

col = input('what column u looking for: ')
if col in df.columns.tolist():
    print("yes")
else:
    print("no")

df_copy = df.copy()

df_copy["total_goals"] = df["home_goal_count"] + df["visiting_goal_count"]
OT = len(df[df["overtime"] > 0])
print(f"{OT} games went into OT")