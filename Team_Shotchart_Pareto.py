# Import more packages
from nba_api.stats.static import teams 

from nba_api.stats.endpoints import shotchartdetail
import pandas as pd

# Initialize an empty DataFrame to store the data
data = pd.DataFrame()
#players we want to look into
superstars = ["Chicago Bulls", "New York Knicks",
             "Los Angeles Lakers", "Dallas Mavericks"]

#pull player ids from superstars
teams_ids = []
for i in superstars:
    teams_ids.append(teams.find_teams_by_full_name(i)[0]['id'])

# Loop through the player IDs
for team_id in teams_ids:
    # Make the API request
    shotlog_all = shotchartdetail.ShotChartDetail(team_id = team_id,
                                            player_id=0,
                                            context_measure_simple = 'FGA', 
                                            season_type_all_star = ['Regular Season', 'Playoffs'])
    team_data = shotlog_all.get_data_frames()[0]

    # Append the player data to the main DataFrame
    data = pd.concat([data, team_data], ignore_index=True)

return data.to_dict(orient='list')