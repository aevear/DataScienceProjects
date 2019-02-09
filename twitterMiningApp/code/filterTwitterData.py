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
def filterData(twitterData):
    #---------------------------------------------------------------------------
    # Set Variables
    #---------------------------------------------------------------------------
    with open('./data/twitterData.json', 'r') as json_data:
        twitterData = json.load(json_data)
    #---------------------------------------------------------------------------
    # Initializing the word counter system
    #---------------------------------------------------------------------------
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via']
    count_all = Counter()
    #---------------------------------------------------------------------------
    # Look for the top five words in each section
    #---------------------------------------------------------------------------
    for tweet in twitterData:
        completeTerms = tweet["text"]
        #Here we will remove the most common terms and things like spaces
        for badTerms in stop:
            completeTerms.strip(badTerms)
        completeTerms = completeTerms.split(" ")
        print(completeTerms)

        '''
        print(completeTerms)
        count_all.update(completeTerms)
        terms_single = set(terms_all)
        # Print the first 5 most frequent words
        print(count_all.most_common(5))

        terms_stop = [term for term in tweet['text'] if term not in stop]
        '''
#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
