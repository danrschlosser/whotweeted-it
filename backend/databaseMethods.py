from pymongo import MongoClient
import datetime



client = MongoClient()
db = client.whoTweetedIt


#Twitter Database Stuff
#------------------------------------------------------------------------------#

#adds a tweet with the given properties and returns the id number of the database entry
def addTweet(username, displayname, tweets, picurl):
	date = datetime.datetime.utcnow()

	tweet = {"username" : username, "displayname" : displayname,"tweets" : tweets, "picUrl" : picurl, "date added" : date}

	return db.tweets.insert(tweet)

#returns a dictionary of style: {"username" : username, "displayname" : displayname,"tweets" : tweets,"date added" : date}
def getTweet(index):
	return db.tweets.find()[index]

#gets size of the tweet database (each document represents one user)
def getTweetDbSize():
	return db.tweets.count()

#wipes the whole tweet database
def wipeTweets():
	db.tweets.remove()



#Score Database
#------------------------------------------------------------------------------#

#the associated collection here is called scores, and it is in the database whoTweetedIt

#adds a person with the given properties and returns the id number of the database entry
def addPerson(name, score):
	shortname = name[:10]
	person = {"name" : shortname , "score" : int(score)}
	return db.scores.insert(person)

#gets size of score database
def getScoreDbSize():
	return db.scores.count()

#returns 10 top scoring people
def getHighScores():
	return sorted(list(db.scores.find()[:]), key=lambda k: k["score"])[::-1][:10]

def isWorthy():
	return getHighScores()[9]['score']

def wipeScores():
	db.scores.remove()

#wipe all but the top 10 high scores
def purgeScores():
	if getScoreDbSize() > 10:
		tempScoreList = getHighScores()
		wipeScores()
		for x in range(10):
			addPerson(tempScoreList[x]['name'], tempScoreList[x]['score'])


def addFillerPeople():
	addPerson('Stringer Bell', 1)
	addPerson('Jimmy McNulty', 1)
	addPerson('Bunk Moreland', 7)
	addPerson('Marlo Stanfield', 1)
	addPerson('Omar Little', 2)
	addPerson('Avon Barksdale', 1)
	addPerson('Frank Sobotka', 1)
	addPerson('Cedric Daniels', 3)
	addPerson('Shakima Greggs', 1)
	addPerson('Bubbles', 1)








