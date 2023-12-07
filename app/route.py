from flask import Flask, render_template
from functions.games import get_games, get_game

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
  games = get_games()
  return render_template("index.html", games=games)

@app.route("/<onegame>")
def game(onegame):
  game = get_game(onegame)
  return render_template("game.html", game=game)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=False)
