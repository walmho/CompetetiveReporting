import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

def makeGraphs(xTitle, xValues, yTitle, yValues, title, tempSave, pieTitle, x, y, pieSave):
    """Create a bar graph of # of occurences using two list values
    Args:
        xValues (list): xValues to graph
        yValues (list): yValues - these are graphed based on amount, not actual value

    Returns:
        Saves graphs in temp files to add to pdf
    """

    sortedX = sorted(xValues)
    sortedY = sorted(yValues, key=yValues.count, reverse = True)

    #price/rating comparison with line of best fit
    plt.title(title, fontsize=18)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)

    theta = np.polyfit(sortedX, sortedY, 1)
    y_line = theta[1] + theta[0] * np.array(sortedX)

    plt.scatter(sortedX, sortedY, label="Rating/Price")
    plt.plot(sortedX, y_line, color="red", label="Line of Best Fit")
    plt.legend()
    plt.savefig(tempSave)
    plt.clf()

    #pie chart
    plt.title(pieTitle, fontsize=18)
    labels = [f"{i} bed" for i in x]

    plt.pie(y)
    plt.legend(labels, loc="best")
    plt.savefig(pieSave)
