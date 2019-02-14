#-------------------------------------------------------------------------------
# Running Twitter Mining App Code - Visualization
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from operator import itemgetter
import matplotlib.pyplot as plt
#-------------------------------------------------------------------------------
# Function for Finding Frequency
#-------------------------------------------------------------------------------
def findFrequency(filteredTweets):
    totalTweets = []
    #---------------------------------------------------------------------------
    # Complile all the twitter text together
    #---------------------------------------------------------------------------
    for tweets in filteredTweets:
        for text in tweets:
            totalTweets.append(text)
    #---------------------------------------------------------------------------
    # Make a dic for most common phrases
    #---------------------------------------------------------------------------
    totalsArray = {}
    for k in totalTweets:
        if k in totalsArray:
            totalsArray[k] = totalsArray[k] + 1
        else:
            totalsArray[k] = 1
    #---------------------------------------------------------------------------
    # make a list for all of them based on highest/lowest value
    #---------------------------------------------------------------------------
    return(sorted(totalsArray.items(), key=itemgetter(1)))
#-------------------------------------------------------------------------------
# Bar Graph for Most Frequent
#-------------------------------------------------------------------------------

def mostFreqBar(filteredTweets):
    orderedTweets = findFrequency(filteredTweets)
    orderedTweets = orderedTweets[::-1]
    #---------------------------------------------------------------------------
    # makes list for the graph
    #---------------------------------------------------------------------------
    namesArray, numberArray = [], []
    for k in orderedTweets[:20]:
        namesArray.append(str(k[0]).strip("\n"))
        numberArray.append(k[1])
    #---------------------------------------------------------------------------
    # Make the Graph
    #---------------------------------------------------------------------------
    # x-coordinates of left sides of bars
    ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # plotting a bar chart
    plt.bar(ticks, numberArray, tick_label = namesArray, width = 0.8, color = ['red', 'green'])
    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')
    # plot title
    plt.title("Most Common Words on Twitter for Topic")
    # function to show the plot
    plt.show()
#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
