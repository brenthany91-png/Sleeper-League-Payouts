from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

SLEEPER = "https://api.sleeper.app/v1"

@app.route("/user/<username>")
def get_user(username):
    r = requests.get(f"{SLEEPER}/user/{username}")
    return jsonify(r.json())

@app.route("/leagues/<user_id>")
def get_leagues(user_id):
    r = requests.get(f"{SLEEPER}/user/{user_id}/leagues/nfl/2025")
    return jsonify(r.json())

@app.route("/league/<league_id>/users")
def get_users(league_id):
    r = requests.get(f"{SLEEPER}/league/{league_id}/users")
    return jsonify(r.json())

@app.route("/league/<league_id>/rosters")
def get_rosters(league_id):
    r = requests.get(f"{SLEEPER}/league/{league_id}/rosters")
    return jsonify(r.json())

@app.route("/league/<league_id>/info")
def get_info(league_id):
    r = requests.get(f"{SLEEPER}/league/{league_id}")
    return jsonify(r.json())

@app.route("/league/<league_id>/matchups/<int:week>")
def get_matchups(league_id, week):
    r = requests.get(f"{SLEEPER}/league/{league_id}/matchups/{week}")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
