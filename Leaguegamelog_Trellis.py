from nba_api.stats.endpoints import leaguegamelog
import pandas as pd

# Initialize an empty DataFrame to store the data
data = pd.DataFrame()

# Loop through the last five seasons
for season in ["2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23"]:
    # Make the API request
    gamelog = leaguegamelog.LeagueGameLog(season=season)
    season_data = gamelog.get_data_frames()[0]

    # Append the season data to the main DataFrame
    data = pd.concat([data, season_data], ignore_index=True)

return data.to_dict(orient='list')