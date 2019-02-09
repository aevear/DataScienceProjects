#-------------------------------------------------------------------------------
# Code Start - Twitter Endless Space Mining Code
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
import json, tweepy, sys
from os import chdir
from tweepy import OAuthHandler
#-------------------------------------------------------------------------------
# Makin da import functions
#-------------------------------------------------------------------------------
def importTokens():
    fi = open("./data/tokens.txt", 'r') #reads in the file that list the before/after file names
    consumer_key = fi.readline().strip("\n") #reads in files
    consumer_secret = fi.readline().strip("\n")
    access_token = fi.readline().strip("\n")
    access_secret = fi.readline().strip("\n")
    return(consumer_key, consumer_secret, access_token, access_secret)
#-------------------------------------------------------------------------------
# Code that Actually Pulls from Twitter
#-------------------------------------------------------------------------------
def pullFromTwitter(query):
    #---------------------------------------------------------------------------
    # Set Variables
    #---------------------------------------------------------------------------
    consumer_key, consumer_secret, access_token, access_secret = importTokens()
    #---------------------------------------------------------------------------
    # Connect into twitter
    #---------------------------------------------------------------------------

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    print("Authenticating now......")
    api = tweepy.API(auth, wait_on_rate_limit=True)
    print("Authenticating done")
    #---------------------------------------------------------------------------
    # Pull Twitter Data
    #---------------------------------------------------------------------------
    max_tweets = 2000

    print("Begining to pull twitter data")
    twitterData = tweepy.Cursor(api.search, q=query).items(max_tweets)
    #---------------------------------------------------------------------------
    # Store data in a JSON file
    #---------------------------------------------------------------------------
    results = []
    with open('data/twitterData.json', 'w') as fileout:
        for tweet in twitterData:
            tweetParts = {}
            tweetParts['created_at']     = str(tweet.created_at)
            tweetParts['text']           = str(tweet.text)
            tweetParts['favorite_count'] = str(tweet.favorite_count)
            tweetParts['lang']           = str(tweet.lang)
            tweetParts['place']          = str(tweet.place)
            tweetParts['entities']       = str(tweet.entities)
            results.append(tweetParts)
        json.dump(results, fileout)

    print("Done pulling data")
    return results

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
