from pymongo import MongoClient
import datetime


client = MongoClient()
db = client.whoTweetedIt


#Twitter Database Stuff 
#------------------------------------------------------------------------------#

#adds a tweet with the given properties and returns the id number of the database entry
def addTweet(username, displayname, tweets):
	date = datetime.datetime.utcnow()

	tweet = {"username" : username, "displayname" : displayname,"tweets" : tweets,"date added" : date}

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

#wipes tweets older than 1 week:
def wipeOneWeek():


#Score Database
#------------------------------------------------------------------------------#

#the associated collection here is called scores, and it is in the database whoTweetedIt

#adds a person with the given properties and returns the id number of the database entry
def addPerson(name, score):
	person = {"name" : name , "score" : score}
	return db.scores.insert(person)


def wipeScores():
	db.scores.remove()
