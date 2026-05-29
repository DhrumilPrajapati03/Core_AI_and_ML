import pandas as pd

df = pd.read_csv('IPLDataSet.csv')
# print(df.head(10))

# k = df.groupby(['city','season'])

# for i,j in k:
#     print(i,j)

team = df.groupby('team1')
print(team.first())   

team_stats = df.groupby('winner').agg(
    total_wins=('winner', 'count'),
    max_runs_margin=('win_by_runs', 'max'),
    max_wickets_margin=('win_by_wickets', 'max')
).reset_index()

# print(team_stats)


toss_stats = df.groupby('toss_decision').agg(
    total_matches=('toss_decision', 'count'),
    avg_runs_margin=('win_by_runs', 'mean')
).reset_index()

# print(toss_stats)

# Group by 'city' and evaluate the matches played and margins
city_stats = df.groupby('city').agg(
    matches_played=('id', 'count'),
    avg_win_runs=('win_by_runs', 'mean'),
    max_win_wickets=('win_by_wickets', 'max')
).reset_index()

# print(city_stats)

# Group by player, count entries, and sort descending
top_players = df.groupby('player_of_match').agg(
    awards_count=('player_of_match', 'count')
).reset_index()

# print(top_players)

matches_at_venue = df.groupby('venue').agg(
    max_runs = ('win_by_runs','max'),
    season = ('season', 'count')
).reset_index()

# print(matches_at_venue)