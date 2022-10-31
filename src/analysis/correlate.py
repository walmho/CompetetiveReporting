import matplotlib.pyplot as plt
import pandas as pd

def barGraphOccurences(xValues, yValues):
    """Create a bar graph of # of occurences using two list values
    Args:
        xValues (list): xValues to graph
        yValues (list): yValues - these are graphed based on amount, not actual value

    Returns:
        Saves graph in temp file to add to pdf
    """
    
    sortedX = pd.Series.sort_values(xValues, ascending=True)
    #sortedY = 

    plt.bar(sortedX, )
