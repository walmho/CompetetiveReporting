# More will be added here as html and css is used - essentially just adding backend analysis data to the frontend
# report to make it look more pretty
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

def findAverage(costValues):
    """ Calculate the average; allows error exceptance

    Args:
        costValues (list): list of ppn values

    Returns:
        average (float): average in costValues list

    """

    try:
        average = sum(costValues)/len(costValues)
    except ZeroDivisionError:
        print(f"list {costValues} may be empty. Defaulting value to 100.")
        average = 100
    return average

#spendDef is the base price required for a house to be considered 'expensive'
def expensiveRatings(costRating, spendDef=100):
    """ Find the ratings of listings >= spendDef

    Args:
        costRating (dict): Cost-Rating relationship
        spendDef (int): The bar for a listing to be considered "expensive"

    Returns:
        expensiveListings (list): list of ratings for all expensive listings in area

    """

    expensiveListings = []
    for listing in costRating:
        if listing >= spendDef:
            expensiveListings.append(costRating[listing])

    return expensiveListings

def cheapRatings(costRating, spendDef=80):
    """ Find the ratings of listings <= spendDef

    Args:
        costRating (dict): Cost-Rating relationship
        spendDef (int): The bar for a listing to be considered "cheap"

    Returns:
        cheapListings (list): list of ratings for all cheap listings in area

    """

    cheapListings = []
    for listing in costRating:
        if listing <= spendDef:
            cheapListings.append(costRating[listing])

    return cheapListings
