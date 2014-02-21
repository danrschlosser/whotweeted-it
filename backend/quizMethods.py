import random
import json
import databaseMethods as db


def makeQuiz():

    random_numbers = random.sample(range(db.getTweetDbSize()), 4)

    tweet1 = db.getTweet(random_numbers[0])
    tweet2 = db.getTweet(random_numbers[1])
    tweet3 = db.getTweet(random_numbers[2])
    tweet4 = db.getTweet(random_numbers[3])

    correct_user_name = tweet1['displayname']
    correct_user_picurl = tweet1['picUrl']
    size_of_tweetlist = len(tweet1['tweets'])
    correct_user_tweet = tweet1['tweets'][random.randrange(0,size_of_tweetlist)]
    correct_user_dict = {'display_name':correct_user_name , 'image' : correct_user_picurl}

    wrong_user_1 = tweet2['displayname']
    wrong_pic_1 = tweet2['picUrl']
    wrong_user_dict1 = {'display_name' : wrong_user_1 , 'image' : wrong_pic_1}

    wrong_user_2 = tweet3['displayname']
    wrong_pic_2 = tweet3['picUrl']
    wrong_user_dict2 = {'display_name' : wrong_user_2 , 'image' : wrong_pic_2}


    wrong_user_3 = tweet4['displayname']
    wrong_pic_3 = tweet4['picUrl']
    wrong_user_dict3 = {'display_name' : wrong_user_3 , 'image' : wrong_pic_3}


    final_user_array = [correct_user_dict, wrong_user_dict1, wrong_user_dict2, wrong_user_dict3]
    random.shuffle(final_user_array)

    d = {"tweet" : correct_user_tweet, "correctUser" : correct_user_name, "candidates" : final_user_array}
    return d


def makeEasyQuiz():

    random_numbers = random.sample(range(db.getEasyTweetDbSize()), 4)

    tweet1 = db.getEasyTweet(random_numbers[0])
    tweet2 = db.getEasyTweet(random_numbers[1])
    tweet3 = db.getEasyTweet(random_numbers[2])
    tweet4 = db.getEasyTweet(random_numbers[3])

    correct_user_name = tweet1['displayname']
    correct_user_picurl = tweet1['picUrl']
    size_of_tweetlist = len(tweet1['tweets'])
    correct_user_tweet = tweet1['tweets'][random.randrange(0,size_of_tweetlist)]
    correct_user_dict = {'display_name':correct_user_name , 'image' : correct_user_picurl}

    wrong_user_1 = tweet2['displayname']
    wrong_pic_1 = tweet2['picUrl']
    wrong_user_dict1 = {'display_name' : wrong_user_1 , 'image' : wrong_pic_1}

    wrong_user_2 = tweet3['displayname']
    wrong_pic_2 = tweet3['picUrl']
    wrong_user_dict2 = {'display_name' : wrong_user_2 , 'image' : wrong_pic_2}


    wrong_user_3 = tweet4['displayname']
    wrong_pic_3 = tweet4['picUrl']
    wrong_user_dict3 = {'display_name' : wrong_user_3 , 'image' : wrong_pic_3}


    final_user_array = [correct_user_dict, wrong_user_dict1, wrong_user_dict2, wrong_user_dict3]
    random.shuffle(final_user_array)

    d = {"tweet" : correct_user_tweet, "correctUser" : correct_user_name, "candidates" : final_user_array}
    return d