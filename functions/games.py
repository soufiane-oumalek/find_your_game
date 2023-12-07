import requests

def get_games():
  first_list = []
  url = "https://www.freetogame.com/api/games?"
  games_list = requests.get(url).json()
  for i in range(0, 20):
    first_list.append(games_list[i])
  return first_list

def get_game(onegame):
  url = "https://www.freetogame.com/api/games?"
  games_list = requests.get(url).json()
  for game in games_list:
    if onegame == game["title"]:
      return game
  return {"error": "this game doesn't exist"}
