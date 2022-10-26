from numpy import average
from dataRetrieval.scrapeData import get_page
from createReport.addAnalysis import dictFromLists, cleanDict, averagePPN, expensiveRatings
from createReport.generateTemplate import pdfTemplate
from sendReport.sendOff import pdfOut

#temp
location = {"city":"Hillsboro", "state":"Oregon", "country":"US"}
n = 10

#Need to add string documentation to all of this
"""An important note is that the Airbnb website displays their best rated / superhost homes FIRST. This means that
as of right now in the code, all scraped ratings are almost always going to be above 4. This makes data analysis
only tell one side of the story. may want to consider updating scraping methods to get a more even mix, or simply
scrape 10x more data when creating the final report.
"""
if __name__ == "__main__":
    outFile = "outputs/output.txt"
    templateFile = "templates/mainLayout.html"
    status, ppN, ratings = get_page(location["city"], location["state"], location["country"], n, debug=False)

    #creating dictionary of cost:rating relationships.
    costRatingRaw = dictFromLists(ppN, ratings)
    #Cleaning the dictionary (ratings are marked as "new" if they are a new listing/have no ratings. This is a no-no)
    costRatingCleaned = cleanDict(float, costRatingRaw)
    ppnAverage = averagePPN(costRatingCleaned)
    unrated = len(costRatingRaw) - len(costRatingCleaned)

    pdfOutput = pdfTemplate(n, ratings, location, ppnAverage, unrated)
    pdfOutput.loadTemplate()
    pdfOut("outputs/updated.html", "outputs/report.pdf")
