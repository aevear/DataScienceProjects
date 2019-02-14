#-------------------------------------------------------------------------------
# Code Start - Twitter Endless Space Mining Code
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
import json, tweepy, string
from os import chdir, getcwd
from collections import Counter
from nltk.corpus import stopwords
#-------------------------------------------------------------------------------
# Importing nltk
#-------------------------------------------------------------------------------
import nltk
#nltk.download('stopwords')
#-------------------------------------------------------------------------------
# Code that Actually Pulls from Twitter
#-------------------------------------------------------------------------------
def filterData(query):
    #---------------------------------------------------------------------------
    # Get JSON data
    #---------------------------------------------------------------------------
    dataName = 'data/twitterData' + query + '.json'
    with open(dataName, 'r') as json_data:
        twitterData = json.load(json_data)
    #---------------------------------------------------------------------------
    # Initializing the word counter system
    #---------------------------------------------------------------------------
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', 'Our', 'I', 'We']
    #---------------------------------------------------------------------------
    # Look for the top five words in each section
    #---------------------------------------------------------------------------
    filteredTweets = []
    for tweet in twitterData:
        completeTerms = tweet["text"].split(" ")
        #Here we will remove the most common terms and things like spaces
        updatedCompleteTerms = set(completeTerms) - set(stop)
        filteredTweets.append(list(updatedCompleteTerms))
    return(filteredTweets)


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
