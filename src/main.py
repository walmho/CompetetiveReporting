from analysis.plots import barGraphOccurences
from dataRetrieval.scrapeData import get_page
from createReport.addAnalysis import dictFromLists, cleanDict, findAverage, expensiveRatings, cheapRatings
from createReport.generateTemplate import pdfTemplate
from sendReport.sendOff import pdfOut

#temp
location = {"city":"Hillsboro", "state":"Oregon", "country":"US"}
n = 1
highPercent = 80
lowPercent = 20

"""An important note is that the Airbnb website displays their best rated / superhost homes FIRST. This means that
as of right now in the code, all scraped ratings are almost always going to be above 4. This makes data analysis
only tell one side of the story. may want to consider updating scraping methods to get a more even mix, or simply
scrape 10x more data when creating the final report.
"""
if __name__ == "__main__":
    plotSave = "./outputs/tempPlot.jpg"
    templateFile = "templates/mainLayout.html"
    status, ppN, ratings, errors = get_page(location["city"], location["state"], location["country"], n, debug=False)

    costRatingRaw = dictFromLists(ppN, ratings)
    costRatingCleaned = cleanDict(float, costRatingRaw)

    barGraphOccurences("Price, Per Night",
    list(costRatingCleaned.keys()), 
    "Rating (out of 5)", 
    list(costRatingCleaned.values()), 
    "Price to Rating Comparison",
    plotSave
    )

    ppnAverage = findAverage(ppN, 2)
    unratedHouses = (len(costRatingRaw) - len(costRatingCleaned))

    highEndListings, topHouse = (expensiveRatings(costRatingCleaned, highPercent))
    highAverage = findAverage(highEndListings.values(), 2)
    cheapListings, lowHouse = (cheapRatings(costRatingCleaned, lowPercent))
    cheapAverage = findAverage(cheapListings.values(), 2)

    pdfOutput = pdfTemplate(
        n, 
        ratings, 
        location, 
        ppnAverage, 
        unratedHouses, 
        highPercent, 
        highAverage, 
        topHouse, 
        lowPercent, 
        cheapAverage, 
        lowHouse,  
        "ppnRatingComparison"

        )
    
    pdfOutput.loadTemplate()
    pdfOut("outputs/updated.html", "outputs/report.pdf")
