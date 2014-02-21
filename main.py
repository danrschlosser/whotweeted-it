""" main.py is the top level script."""

from backend import databaseMethods as db
from backend import quizMethods as q
from backend.twitter.twitterAuth import tokens

#get_tweet_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mileycyrus&count=3"

# Import the Flask Framework
from flask import Flask, render_template, redirect, url_for, session
app = Flask(__name__)
app.config["DEBUG"] = True

app.secret_key = tokens.cookie_secret
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
	session["score"] = 0
	session["best"] = 0
	return redirect(url_for('quiz'))

@app.route('/favicon.ico')
def favicon():
	return redirect(url_for('static', filename='img/favicon.ico'))

@app.route('/quiz')
def quiz():
	data = q.makeQuiz()
	if session["score"] is None or session["best"] is None:
	    return render_template("quiz.html", data=data, score=0, best=0)
	else:
		return render_template("quiz.html", data=data, score=session["score"], best=session["score"])

@app.route('/continue/<score>/<best>')
def cont(score, best):
	session["score"] = int(score)
	session["best"] = max(int(score), int(best))
	return redirect(url_for('quiz'))

@app.route('/donegoofed')
def goofed():
	if session["score"] > db.isWorthy():
		return redirect(url_for('submit'))
	else:
		session["best"] = max(session["best"], session["score"])
		session["score"] = 0
		return redirect(url_for('quiz'))

@app.route('/submit')
def submit():
	return render_template("submit.html", score=session["score"])

@app.route('/leaderboard')
def leaderboard():
	people = db.getHighScores()
	return render_template("scores.html", people=people)

@app.route('/leaderboardcutoff')
def isWorthy():
	return db.isWorthy()

@app.route('/post/<name>/<score>', methods=["GET", "POST"])
def post(name, score):
	print "posting:" + name + score
	db.addPerson(name, score)
	return "Posted: " + name + ", " + score

@app.route('/about')
def about():
    """Return some friendly info."""
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")

