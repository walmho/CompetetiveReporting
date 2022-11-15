from multiprocessing.sharedctypes import Array
import numpy as np
import pandas as pd

def dictFromLists(keys, values):
    """ Create a dictionary from two lists

    Args:
        keys (list): first list contains keys for new dict
        values (list): second list contains values for new dict

    Returns:
        dict (dict): dictionary with {keys:values} corresponding

    """

    return dict(map(lambda i,j : (i,j), keys, values))

def cleanDict(removeType, dictionary):
    """ Remove all but one type of value from a dict

        Args:
            removeType (type): var type to convert to / keep
            dictionary (dict): dictionary to edit

        Returns:
            cleanDictionary (dict): dictionary with all other types purged

    """

    cleanDictionary = {}
    for key in dictionary:
        try:
            dictionary[key] = removeType(dictionary[key])
            cleanDictionary[key] = dictionary[key]
        #Bypass if house has no ratings, don't add it to cleaned dictionary
        except ValueError:
            pass
    
    # print(f"{dictionary}\n{cleanDictionary}\n\n\n{len(dictionary)}\n{len(cleanDictionary)}")
    return cleanDictionary

def findAverage(costValues, roundPt):
    """ Calculate the average; allows error exceptance

    Args:
        costValues (list): list of ppn values
        roundPt (int): # of decimal points to round to

    Returns:
        average (float): average in costValues list

    """

    try:
        average = round((sum(costValues)/len(costValues)), roundPt)
    except ZeroDivisionError:
        print(f"list {costValues} may be empty. Defaulting value to 100.")
        average = 100
    return average

#spendDef is the base price required for a house to be considered 'expensive'
def expensiveRatings(costRating, percentile):
    """ Find the top expensive listings above given percentTile

    Args:
        costRating (dict): Cost-Rating relationship
        percentile (int): The percenttile threshold to find houses more expensive than

    Returns:
        topHouses (dict): list of ratings for all expensive listings in area
        top (int): most expensive housing price in area

    """

    sortedListings = dict(sorted(costRating.items()))

    #calculates percentile
    threshold = (np.percentile(list(sortedListings.keys()), percentile))
    topHouses = {}
    for key in sortedListings.keys():
        if key >= threshold:
            topHouses[key] = sortedListings[key]
    top = max(topHouses)

    return topHouses, top

def cheapRatings(costRating, percentile):
    """ Find the cheapest listings below given percentTile

    Args:
        costRating (dict): Cost-Rating relationship
        percentile (int): The percenttile threshold to find houses cheaper than

    Returns:
        lowHouses (dict): dict of ratings for all cheap listings in area
        low (int): cheapest housing price in area

    """

    sortedListings = dict(sorted(costRating.items()))

    #calculates percentile
    threshold = (np.percentile(list(sortedListings.keys()), percentile))
    lowHouses = {}
    for key in sortedListings.keys():
        if key <= threshold:
            lowHouses[key] = (sortedListings[key])
    low = min(lowHouses)

    return lowHouses, low

def bedStatistics(bedList):
    """ Find stats about # of beds in area

    Args:
        bedList (list): # of beds per each listing

    Returns:
        bedMin (int): least # of beds per listing
        bedMax (int): highest # of beds per listing
        bedAverage (int): average # of beds, rounded
        bedAmounts (dict): the number of listings that had each number of beds

    """

    tempArray = np.array(bedList)
    unique = np.unique(tempArray)

    bedMin = min(bedList)
    bedMax = max(bedList)
    bedAverage = round(sum(bedList)/len(bedList))
    bedCounts = pd.Series(bedList).value_counts()
    bedCounts = pd.Series.tolist(bedCounts)

    bedAmounts = dictFromLists(unique, bedCounts)

    return bedMin, bedMax, bedAverage, bedAmounts