#-------------------------------------------------------------------------------
# Running Twitter Mining App Code
#-------------------------------------------------------------------------------
import sys
from os import chdir, system
from code.twitterMining import pullFromTwitter
from code.filterTwitterData import filterData
#-------------------------------------------------------------------------------
# Run Program
#-------------------------------------------------------------------------------
query = str(sys.argv[1])
#-------------------------------------------------------------------------------
# 1 : Pull Data : This part pulls 2 weeks worth of data from twitter on a query
#-------------------------------------------------------------------------------
twitterData = pullFromTwitter(query)
#-------------------------------------------------------------------------------
# 2 : Pull Data : This part pulls 2 weeks worth of data from twitter on a query
#-------------------------------------------------------------------------------
filteredTweets = filterData(twitterData)

#print(filteredTweets)










#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
