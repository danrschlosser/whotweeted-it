import json
import tokens

import oauth2 as oauth

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


print get_tweets("justinbieber")