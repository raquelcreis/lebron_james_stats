# Imports
import pandas as pd
import numpy as np

from nba_api.stats.static import players
from nba_api.stats.static import teams 

import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',250)

# Creating a DataFrame with all NBA players
player_dict = players.get_players()
players = pd.DataFrame(player_dict)
print("Total of players:",players.shape[0])

# Finding LeBron James ID
lebronId = players.id[players.full_name == 'LeBron James'].to_list()[0]

#Fetching All LeBron Stats
from nba_api.stats.endpoints import playercareerstats
lebronCareer = playercareerstats.PlayerCareerStats(player_id = lebronId)
lebronCareer = lebronCareer.get_data_frames()[0]

#Creating a column with a cumulative sum on PTS
lebronCareer['SUM_PTS'] = lebronCareer['PTS'].cumsum()

# Displaying Sum of Points 
print("Total Scores of LeBron until today:",lebronCareer.SUM_PTS.max())

# Checking Cumulative Sum of PTS over time
sns.set_style("whitegrid")
plt.figure(figsize=(20,4))
c = sns.barplot(data = lebronCareer, x='SEASON_ID',y='SUM_PTS')
plt.xlabel('Season')
plt.ylabel('Points')
plt.title('LeBron James Scoring Stats Over Time')
plt.show(c)