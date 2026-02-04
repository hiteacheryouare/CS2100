import pandas as bamboo
from pandas.api.types import is_integer_dtype
import numpy as numbers

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

print(df_copy["total_goals"].value_counts())
print(df_copy.sort_values(by=["date, attendance"], ascending=[True, False], kind="quicksort"))

if is_integer_dtype(df_copy["periods"]):
    print("yes.")
else:
    print("no")

df_copy["game_length"] = df_copy["periods"].map({
    3: "standard",
    4: "OT",
    5: "NOTOT",
    6: "THREEOT"
})

coerce = numbers.corrcoef

r = coerce(df_copy["attendance"], df_copy["home_goal_count"]),