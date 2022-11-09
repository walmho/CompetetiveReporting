import matplotlib.pyplot as plt
import pandas as pd

def barGraphOccurences(xTitle, xValues, yTitle, yValues, title, tempSave):
    """Create a bar graph of # of occurences using two list values
    Args:
        xValues (list): xValues to graph
        yValues (list): yValues - these are graphed based on amount, not actual value

    Returns:
        Saves graph in temp file to add to pdf
    """

    sortedX = sorted(xValues)
    sortedY = sorted(yValues, key=yValues.count, reverse = True)

    plt.title(title)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.bar(sortedX, sortedY, width=2)

    plt.savefig(tempSave)
