from gettext import find
from numpy import average
from analysis.correlate import barGraphOccurences
from dataRetrieval.scrapeData import get_page
from analysis.correlate import barGraphOccurences
from createReport.addAnalysis import dictFromLists, cleanDict, findAverage, expensiveRatings, cheapRatings
from createReport.generateTemplate import pdfTemplate
from sendReport.sendOff import pdfOut

#temp
location = {"city":"Hillsboro", "state":"Oregon", "country":"US"}
n = 2

#Could also automate what is considered to be "cheap" and "expensive" based on the mean, median, etc.
costBar = 120
cheapBar = 80

"""An important note is that the Airbnb website displays their best rated / superhost homes FIRST. This means that
as of right now in the code, all scraped ratings are almost always going to be above 4. This makes data analysis
only tell one side of the story. may want to consider updating scraping methods to get a more even mix, or simply
scrape 10x more data when creating the final report.
"""
if __name__ == "__main__":
    outFile = "outputs/output.txt"
    templateFile = "templates/mainLayout.html"
    status, ppN, ratings = get_page(location["city"], location["state"], location["country"], n, debug=False)

    costRatingRaw = dictFromLists(ppN, ratings)
    costRatingCleaned = cleanDict(float, costRatingRaw)
    barGraphOccurences("Price, Per Night", list(costRatingCleaned.keys()), "Rating (out of 5)", list(costRatingCleaned.values()), "Price to Rating Comparison")

    ppnAverage = findAverage(ppN)
    unratedHouses = (len(costRatingRaw) - len(costRatingCleaned))

    highEndListings = round(findAverage(expensiveRatings(costRatingCleaned, costBar)), 2)
    cheapListings = round(findAverage(cheapRatings(costRatingCleaned, cheapBar)), 2)

    pdfOutput = pdfTemplate(n, ratings, location, ppnAverage, unratedHouses, costBar, highEndListings, cheapBar, cheapListings)
    pdfOutput.loadTemplate()
    pdfOut("outputs/updated.html", "outputs/report.pdf")
