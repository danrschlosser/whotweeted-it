""" main.py is the top level script."""

from quizmaker import get_methods

get_tweet_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mileycyrus&count=3"
# Import the Flask Framework
from flask import Flask, render_template, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True 
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template("quiz.html")

@app.route('/about')
def about():
    """Return some friendly info."""
    return render_template("about.html")

def makedict():
	return jsonify(get_methods.getdict(get_tweet_url))

@app.route('/scores')
def scores():
    """Return the leaderboard."""
    return render_template("scores.html")

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404
