import json
from twitter import tokens
import oauth2 as oauth
import databaseMethods as db
import tweetFilters as filters

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


#loads the tweets database with roughly 20 tweets from the given username
def putTweetInDatabase(username):

    depth = 50
    #number of tweets to add

    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + username + "&count=" + str(depth) + "&exclude_replies=true" + "&include_rts=false"
    dictionary = getdict(url)
    listoftweets = dictionary['content']
    tweets = list()

    try:
        display_name = listoftweets[0]['user']['name']
        pic_url = listoftweets[0]['user']['profile_image_url']
        
        for tweet in listoftweets:
            tweets.append(filters.filter(tweet['text']))

        db.addTweet(username, display_name, tweets, pic_url)

    except:
        print(listoftweets)
        print(username)


def fillTweetDatabase():
    with open('userslist.py', 'r') as f:
        string = f.read()
        users = eval('[' + string + ']')

    for user in users:
        putTweetInDatabase(user)


