# Import the 'requests'
import requests

# Function to retrieve a list of games grouped by genre
def get_games():
    genres = {}
    # API endpoint URL for fetching game data
    url = "https://www.freetogame.com/api/games?"
    games_list = requests.get(url).json()
    for i in range(0, 100):
        if games_list[i]["genre"] not in genres:
            genres[games_list[i]["genre"]] = []
        genres[games_list[i]["genre"]].append(games_list[i])

    for genre in list(genres.keys()):
        if len(genres[genre]) < 4:
            del genres[genre]
    return genres

# Function to retrieve details about a specific game
def get_game(onegame):
    # API endpoint URL for fetching game data
    url = "https://www.freetogame.com/api/games?"
    games_list = requests.get(url).json()
    for game in games_list:
        onegame = onegame.replace("%20", " ")
        lower_name = onegame.lower()
        lower_title = game["title"].lower()
        if lower_name == lower_title.lower() or (lower_title.startswith(lower_name) and len(onegame) > 3):
            return game
    return {"error": "this game doesn't exist in our platform"}
