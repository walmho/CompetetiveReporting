from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import createBase, printOut, dateReport

if __name__ == "__main__":
    status, houseList, ratings = get_page("Hillsboro", "Oregon", "US", debug=False)

    dateReport("templates/output.txt")
    for index in range(len(houseList)):
        basic = createBase("basics.txt", index+1, houseList[index], ratings[index])
        printOut("templates/output.txt", basic)
    