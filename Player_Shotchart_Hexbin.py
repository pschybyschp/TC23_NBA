# Import more packages
from nba_api.stats.static import players

from nba_api.stats.endpoints import shotchartdetail
import pandas as pd

# Initialize an empty DataFrame to store the data
data = pd.DataFrame()
#players we want to look into
superstars = ["Stephen Curry", "Kevin Durant",
             "Lebron James"]

#pull player ids from superstars
player_ids = []
for i in superstars:
    player_ids.append(players.find_players_by_full_name(i)[0]['id'])

# Loop through the player IDs
for player_id in player_ids:
    # Make the API request
    shotlog_all = shotchartdetail.ShotChartDetail(team_id = 0,
                                            player_id=player_id,
                                            context_measure_simple = 'FGA', 
                                            season_type_all_star = ['Regular Season', 'Playoffs'])
    player_data = shotlog_all.get_data_frames()[0]

    # Append the player data to the main DataFrame
    data = pd.concat([data, player_data], ignore_index=True)

return data.to_dict(orient='list')