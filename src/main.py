from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import txtTemplate

if __name__ == "__main__":
    status, houseList, ratings = get_page("Hillsboro", "Oregon", "US", debug=False)

    txtTemplate.dateReport("templates/output.txt")
    for index in range(len(houseList)):
        basic = txtTemplate.createBase("basics.txt", index+1, houseList[index], ratings[index])
        txtTemplate.printOut("templates/output.txt", basic)
    