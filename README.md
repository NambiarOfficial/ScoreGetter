# ScoreGetter
A basic python script that fetches live scores from Cricbuzz and displays information in a terminal.

# Libraries used 
-Python3 requests module
-Python3 BeautifulSoup

The site fetches a json file that has the latest match data and reloads it regularly. The requests module goes to live-scores section on Cricbuzz and fetches the match-id for the current live match. This id is then used to fetch the json file and parse it to get the required data

Displayed information includes 
- Scores of teams
- Current Run Rate
- Required Run Rate (in the second innings)
- Runs scored by each batsman
- Bowling figures for each bowler
- History of past few overs
- 2 or 3 snippets of commentary

