# More will be added here as html and css is used - essentially just adding backend analysis data to the frontend
# report to make it look more pretty
def dictFromLists(keys, values):
    return dict(map(lambda i,j : (i,j) , keys,values))

def cleanDict(removeType, dictionary):
    """ Remove all specific type of value from a dict

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

def averagePPN(costValues):
    try:
        average = sum(costValues)/len(costValues)
    except ZeroDivisionError:
        print(f"list {costValues} may be empty. Defaulting value to 100.")
        average = 100
    return average

#spendDef is the base price required for a house to be considered 'expensive'
def expensiveRatings(costRating, spendDef=100):
    pass
