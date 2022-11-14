import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

def makeGraphs(xTitle, xValues, yTitle, yValues, title, tempSave):
    """Create a bar graph of # of occurences using two list values
    Args:
        xValues (list): xValues to graph
        yValues (list): yValues - these are graphed based on amount, not actual value

    Returns:
        Saves graph in temp file to add to pdf
    """

    sortedX = sorted(xValues)
    sortedY = sorted(yValues, key=yValues.count, reverse = True)

    plt.title(title, fontsize=18)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)

    theta = np.polyfit(sortedX, sortedY, 1)

    y_line = theta[1] + theta[0] * np.array(sortedX)

    plt.scatter(sortedX, sortedY, label="Rating/Price")
    plt.plot(sortedX, y_line, color="red", label="Line of Best Fit")

    plt.legend()

    plt.savefig(tempSave)
