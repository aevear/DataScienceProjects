#-------------------------------------------------------------------------------
# Running Twitter Mining App Code
#-------------------------------------------------------------------------------
import sys
from os import chdir, system
from code.twitterMining import pullFromTwitter
from code.filterTwitterData import filterData
from code.visualizationScripts import mostFreqBar
#-------------------------------------------------------------------------------
# Run Program
#-------------------------------------------------------------------------------
query = str(sys.argv[1])
#-------------------------------------------------------------------------------
# 1 : Pull Data : This part pulls 2 weeks worth of data from twitter on a query
#-------------------------------------------------------------------------------
pullFromTwitter(query) #the first thing that we want to look at
#-------------------------------------------------------------------------------
# 2 : Filters and sorts tweet text data
#-------------------------------------------------------------------------------
filteredTweets = filterData(query)
#-------------------------------------------------------------------------------
# 3 : Graph the data
#-------------------------------------------------------------------------------
#print(filteredTweets)
mostFreqBar(filteredTweets)





#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
