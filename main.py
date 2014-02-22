""" main.py is the top level script."""

#Needed for gunicorn
#############################################
from werkzeug.contrib.fixers import ProxyFix
#############################################

from backend import databaseMethods as db
from backend import quizMethods as q
from backend import easymode as easy
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
	session["started"] = True
	session["gameover"] = False
	session["score"] = 0
	session["best"] = session.get("best") or 0
	return redirect(url_for('quiz'))


@app.route('/favicon.ico')
def favicon():
	return redirect(url_for('static', filename='img/favicon.ico'))

@app.route('/quiz')
def quiz():
	if session.get("started") is None:
		session["started"] = True
		session["gameover"] = False
		session["score"] = 0
		session["best"] = 0

	session["gameover"] = False
	data = q.makeQuiz()
	if session.get("score") is None or session.get("best") is None:
		return render_template("quiz.html", data=data, score=0, best=0)
	else:
		return render_template("quiz.html", data=data, score=session["score"], best=session["best"])

@app.route('/continue/<score>/<best>')
def cont(score, best):
	if not session["gameover"]:
		session["score"] = int(score)
		session["best"] = max(session["best"], session["score"])
	return redirect(url_for('quiz'))

@app.route('/donegoofed')
def goofed():
	session["gameover"] = True
	if session["score"] > db.isWorthy():
		return redirect(url_for('submit'))
	else:
		session["best"] = max(session["best"], session["score"])
		session["score"] = 0
		return redirect(url_for('quiz'))

@app.route('/submit')
def submit():
	score = session["score"]
	session["score"] = 0
	return render_template("submit.html", score=score, best=session["best"])

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



######################___EASYMODE____###################################

@app.route('/easymode')
def easymode():
	session["easy_started"] = True

	if session.get("easy_started") is None:
		session["easy_score"] = 0
		session["easy_best"] = session.get("easy_best") or 0
		session["easy_gameover"] = False
	
	data = q.makeEasyQuiz()
	if session["easy_score"] is None or session["easy_best"] is None:
		return render_template("easymode.html", data=data, score=0, best=0)
	else:
		return render_template("easymode.html", data=data, score=session["easy_score"], best=session["easy_best"])

@app.route('/easycontinue/<score>/<best>')
def easycont(score, best):
	if not session["gameover"]:
		session["easy_score"] = int(score)
		session["easy_best"] = max(session["easy_best"], session["easy_score"])
	return redirect(url_for('easymode'))

@app.route('/easyfail')
def easygoofed():
	session["easy_gameover"] = True
	session["easy_best"] = max(session["easy_best"], session["easy_score"])
	session["easy_score"] = 0
	return redirect(url_for('easymode'))


###############################################################




@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

