""" main.py is the top level script."""

from quizmaker import get_methods as get

get_tweet_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mileycyrus&count=3"
# Import the Flask Framework
from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
app = Flask(__name__)
app.config["DEBUG"] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
    return redirect(url_for('quiz', messages=json.dumps({"score": 0})))

@app.route('/favicon.ico')
def favicon():
	return redirect(url_for('static', filename='img/favicon.ico'))

@app.route('/quiz')
def quiz():
	if request.args["messages"] is None:
	    return render_template("quiz.html", data=get.getQuizData(), score=0)
	else:
		messages = request.args['messages']
		data = get.getQuizData()
		print data
		return render_template("quiz.html", data=data, score=json.loads(messages)["score"])

@app.route('/continue/<score>')
def cont(score):
	return redirect(url_for('quiz', messages=json.dumps({"score": score})))

@app.route('/donegoofed/<score>')
def goofed(score):
	return redirect(url_for('submit', messages=json.dumps({"score": score})))

@app.route('/submit')
def submit():
	messages = request.args['messages']
	return render_template("submit.html", score=json.loads(messages)["score"])

@app.route('/leaderboard')
def leaderboard():
	people = get.getHighScores()
	return render_template("scores.html", people=people)

@app.route('/post/<name>/<score>', methods=["GET", "POST"])
def post(name, score):
	print "posting:" + name + score
	person = get.loadPerson(name, score)
	return "Posted: " +person.name + ", " + person.score

@app.route("/clear")
def clear():
	return get.emptyDatabase()

@app.route('/about')
def about():
    """Return some friendly info."""
    return render_template("about.html")

def makedict():
	return jsonify(get.getdict(get_tweet_url))

@app.route('/generate')
def generate():
	return get.generate_database("quiz_database.json")


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404
