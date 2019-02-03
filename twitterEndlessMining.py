#-------------------------------------------------------------------------------
# Code Start - Twitter Endless Space Mining Code
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
import tweepy
import json
from tweepy import OAuthHandler
#-------------------------------------------------------------------------------
# Set Variables
#-------------------------------------------------------------------------------
consumer_key = 'K249vTrdxDLpRRk7fcq7uGyVE'
consumer_secret = 'UVNezu2wUc0oAi4oXXcsO8iPXtFcd4D0dCRpnc4p8CcY1A4L9O'
access_token = '33096980-yTCFWw1uesYJrq8pnAN7yVP42qMXWyAKu8fQEeTga'
access_secret = 'U65cT6qvzP4snI6fgKL3XVcqMVtzzNlItvzIGdYjnGGYW'
#-------------------------------------------------------------------------------
# Connect into twitter
#-------------------------------------------------------------------------------
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

print("Authenticating now......")
api = tweepy.API(auth, wait_on_rate_limit=True)
print("Authenticating done")
#-------------------------------------------------------------------------------
# Pull Twitter Data
#-------------------------------------------------------------------------------
query = 'endlessspace2'
max_tweets = 2000

print("Begining to pull twitter data")
twitterData = tweepy.Cursor(api.search, q=query).items(max_tweets)
#-------------------------------------------------------------------------------
# Store data in a JSON file
#-------------------------------------------------------------------------------
#with open("data_file.json", "w") as write_file:
#    json.dump(twitterData, write_file)

#for tweet in twitterData:
#    print(json.dumps("yo"))
    #print(json.dumps(tweet.text))


count = 0
with open("data_file.json", "w") as write_file:
    for tweet in twitterData:
        print(tweet.created_at, tweet.text)
        json.dump(tweet, write_file)
        count =+ 1

'''
print(json.dumps(twitterData))

for tweet in twitterData:
    print(tweet.created_at, tweet.text)
    print(json.dumps(tweet))
'''
