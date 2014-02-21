import databaseMethods as db
import twitterMethods as tweet


users = "coffee_dad", "big_ben_clock", "notapoliceman", "officialjaden"

def fillEasy():
    for user in users:
        putEasyTweetInDatabase(user)

