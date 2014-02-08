from __future__ import print_function
import google.appengine.api as oauth
import json
from twitterAuth import tokens
import random


userslist = ['katyperry', 'justinbieber', 'BarackObama', 'ladygaga', 'taylorswift13', 'britneyspears', 'rihanna', 'jtimberlake', 'JLo', 'TheEllenShow', 'Cristiano', 'shakira', 'Oprah', 'Pink', 'ddlovato', 'OfficialAdele', 'Harry_Styles', 'KimKarsashian', 'aliciakeys', 'KAKA', 'selenagomez', 'BrunoMars', 'onedirection', 'NICKIMINAJ', 'NIALLOFFICIAL', 'Eminem', 'MileyCyrus', 'pitbull', 'aplusk', 'Real_Liam_Payne', 'LilTunechi', 'Louis_Tomlinson', 'MariahCarey', 'BillGates', 'AvrilLavigne', 'Drake', 'davidguetta', 'chrisbrown', 'beyonce', 'ArianaGrande', 'ParisHilton', 'wizkhalifa', 'RyanSeacrest', 'jimcarrey', 'emwatson', 'zaynmalik', 'KingJames', 'xtina', 'jimmyfallon', 'iamwill', 'ashleytisdale', 'snoopdogg', 'tyrabanks', 'fcbarcelona', 'alejandrosanz', 'charliesheen', 'kourtneykardash', 'kanyewest','conanobrien', 'ricky_martin', 'kevinhart4real', 'carlyraejepsen', 'neymarjr', 'iamdiddy', 'kelly_clarkson', 'simoncowell', 'danieltosh','khloekardashian', 'usher', 'leodicaprio', 'juanes', 'edsheeran', 'dalailama', 'shaq', 'lmfao', 'big_ben_clock', 'coffee_dad', 'NotAPoliceman', 'The_HelenKeller', 'ElBloombito']
get_tweet_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mileycyrus&count=3"
userlisttest = ['justinbieber', 'BarackObama']

#PUT Dat shit in a secret file or something
API_key = tokens.API_key
API_secret = tokens.API_secret
Access_token = tokens.Access_token
Access_token_secret = tokens.Access_token_secret

def oauth_req(url):


    consumer = oauth.Consumer(API_key, API_secret)
    token = oauth.Token(Access_token, Access_token_secret)
    client = oauth.Client(consumer, token)

    resp, content = client.request(
        url,
        method="GET",

        #headers=http_headers,
        #force_auth_header=True
    )
    return content


def getdict(url):
    response = json.loads(oauth_req(url).encode('utf-8'))
    return {"content": response}

#username, depth of tweet in stack returns
def get_tweets(username):

    depth = 15
    #number of tweets to add

    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + username + "&count=" + str(depth) + "&exclude_replies=true" + "&include_rts=false"
    dictionary = getdict(url)
    listoftweets = dictionary['content']

    try:
        display_name = listoftweets[0]['user']['name']
        pic_url = listoftweets[0]['user']['profile_image_url']

    except:
        print(listoftweets)
        print(username)

    dict_to_return = {username : {
                "display name": display_name,
                "tweets": [],
                "picurl": pic_url
                }}

    for tweet in listoftweets:

        #if !hasturl(str(tweet)):
        dict_to_return[username]['tweets'].append(tweet['text'])


    return dict_to_return

def hasturl(tweet):
    if tweet.find("t.co") != -1:
        return True
    else:
        return False


def generate_database(filename):
    myfile = open(filename, 'w')

    final_dictionary = dict()

    for user in userslist:
        final_dictionary.update(get_tweets(user))
    string = json.dumps(final_dictionary)
    myfile.write(string)
    return string


def getQuizData():

    with open('quizmaker/quiz_database.json', 'r') as f:
        s = f.read()
        dictionary = json.loads(s.encode('utf-8'))
    random_numbers = random.sample(range(len(dictionary)), 4)

    correct_user_name = dictionary[userslist[random_numbers[0]]]['display name']

    correct_user_picurl = dictionary[userslist[random_numbers[0]]]['picurl']
    size_of_tweetlist = len(dictionary[ userslist[random_numbers[0]] ]['tweets'])
    correct_user_tweet = dictionary[ userslist[random_numbers[0]] ]['tweets'][random.randrange(0,size_of_tweetlist)]
    correct_user_dict = {'display_name':correct_user_name , 'image' : correct_user_picurl}

    wrong_user_1 = dictionary[userslist[random_numbers[1]]]['display name']
    wrong_pic_1 = dictionary[userslist[random_numbers[1]]]['picurl']
    wrong_user_dict1 = {'display_name' : wrong_user_1 , 'image' : wrong_pic_1}

    wrong_user_2 = dictionary[userslist[random_numbers[2]]]['display name']
    wrong_pic_2 = dictionary[userslist[random_numbers[2]]]['picurl']
    wrong_user_dict2 = {'display_name' : wrong_user_2 , 'image' : wrong_pic_2}


    wrong_user_3 = dictionary[userslist[random_numbers[3]]]['display name']
    wrong_pic_3 = dictionary[userslist[random_numbers[3]]]['picurl']
    wrong_user_dict3 = {'display_name' : wrong_user_3 , 'image' : wrong_pic_3}

    #order_numbers = random.sample(range(4),4)

    final_user_array = [correct_user_dict, wrong_user_dict1, wrong_user_dict2, wrong_user_dict3]
    random.shuffle(final_user_array)

    d = {"tweet" : correct_user_tweet, "correctUser" : correct_user_name, "candidates" : final_user_array}
    return d

# generate_database('quiz_database.json')

#getQuizData()

#for users in userslist:
#   print users + ":  " + get_random_tweet(str(users)).encode('utf-8')


