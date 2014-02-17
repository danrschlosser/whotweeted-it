from pymongo import MongoClient
import pymongo
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
	person = {"name" : name , "score" : score}
	return db.scores.insert(person)

#gets size of score database
def getScoreDbSize():
	return db.scores.count()

#returns 10 top scoring people
def getHighScores():
	scoreList =  list()
	for x in range(10):
		try:
			scoreList.append(db.scores.find()[0:(getScoreDbSize() - 1)].sort(u'score' , -1)[x])
		except:
			print "Index out of bounds. Need more than 10 in score list"

	return scoreList

def wipeScores():
	db.scores.remove()

#wipe all but the top 10 high scores
def purgeScores():
	if getScoreDbSize() > 10:
		tempScoreList = getHighScores()
		wipeScores()
		for x in range(10):
			addPerson(tempScoreList[x]['name'], tempScoreList[x]['score'])

