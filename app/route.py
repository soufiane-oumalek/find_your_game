#import models
from flask import Flask, render_template
from functions.games import get_games, get_game


app = Flask(__name__)
app.url_map.strict_slashes = False

# Define a route for the home page ("/")
@app.route("/")
def home():
   # Call the 'get_games' function to retrieve a list of games
  games = get_games()
  return render_template("index.html", games=games)

@app.route("/<onegame>")
# Call the 'get_game' function with the game parameter to retrieve details about a specific game
def game(onegame):
  game = get_game(onegame)
  return render_template("game.html", game=game)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=False)
