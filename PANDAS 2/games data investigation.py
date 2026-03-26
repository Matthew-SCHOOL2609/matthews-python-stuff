import pandas as pd
import matplotlib.pyplot as plt
# import libraries

games = pd.read_csv("steam_games_2026.csv") # read csv file

games.columns = games.columns.str.strip().str.lower().str.replace(" ", "_")
# clean columns to lowercase and replace space with underscore

games = games.sample(101)

print("Columns:", list(games.columns))
# prints list of columns

games = games.drop_duplicates()
games = games.dropna() # cleaning. dropna() removes NaN (Not a Number) values, drop_duplicates removes duplicate entries

print("\nSelected columns from games:")

games = games.drop(columns = ["appid", "primary_genre", "all_tags", "price_usd", "discount_pct", "review_score_pct", "total_reviews", "steam_deck_status", "24h_peak_players"])


print(games)
