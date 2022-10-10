from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import txtTemplate

if __name__ == "__main__":
    outFile = "outputs/output.txt"
    #ppN = price per night
    status, ppN, ratings = get_page("Hillsboro", "Oregon", "US", debug=False)
    txtTemplate.dateReport(outFile)

    for index in range(len(ppN)):
        basic = txtTemplate.createBase("basics.txt", index+1, ppN[index], ratings[index])
        txtTemplate.printOut(outFile, basic)
