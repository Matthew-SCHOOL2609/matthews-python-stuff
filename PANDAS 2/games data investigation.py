import pandas as pd
import matplotlib.pyplot as plt
# import libraries

games = pd.read_csv("steam_games_2026.csv") # read csv file

games.columns = games.columns.str.strip().str.lower().str.replace(" ", "_")
# clean columns to lowercase and replace space with underscore

games = games.sample(100)

print("Columns:", list(games.columns))
# prints list of columns

games = games.drop_duplicates()
games = games.dropna() # cleaning

print("\nSelected columns from games:")
games_alt1 = games[["name", "release_date", "primary_genre", "estimated_owners"]]
print(games_alt1)

print(games.describe())