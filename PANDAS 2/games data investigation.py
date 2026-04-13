# to mr shields

# im gonna be real with you i cannot do anything with matplotlib
# like i tried looking it up on google but everything that came up was genuinely indecipherable
# sorry

import pandas as pd
import matplotlib.pyplot as plt
# import libraries

games = pd.read_csv("steam_games_2026.csv") # read csv file

games.columns = games.columns.str.strip().str.lower().str.replace(" ", "_")
# clean columns to lowercase and replace space with underscore

games = games.sample(101) # decrease sample size because its overwhelming

print("Columns:", list(games.columns))
# prints list of columns

games = games.drop_duplicates()
games = games.dropna() # cleaning. dropna() removes NaN (Not a Number) values, drop_duplicates removes duplicate entries

games = games.drop(columns = ["appid", "primary_genre", "all_tags", "price_usd", "discount_pct", "review_score_pct", "total_reviews", "steam_deck_status", "24h_peak_players"])
# drops unnecessary columns

top_games_owner_count = games.sort_values(by="estimated_owners", ascending = False)
# makes a variable called top_games with value being the estimated amount of owners (which we will take as fact), then sorting the values from highest
# to lowest in number (e.g. 0 is last)

print("\n Sorted top games by owner count:")

print(top_games_owner_count)


# --------------------------------------
# anything after this line is done after the due date of the project (i did not have this laptop with me to complete this program and could not go to
# school because of easter holidays. i am so screwed
# --------------------------------------

gamesByOwnerCount = top_games_owner_count

print(gamesByOwnerCount.describe())

print(" ") # prints a blank line for spacing in shell

print(gamesByOwnerCount["estimated_owners"].value_counts())

grouped = gamesByOwnerCount.groupby("name")["estimated_owners"].mean()
print(grouped)

# i genuinely am unable to figure out how to graph this. im sorry

gamesByOwnerCount.to_csv("cleaned_data.csv", index=False)
