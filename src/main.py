from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import createBase

if __name__ == "__main__":
    status, houseList = get_page("Hillsboro", "Oregon", "US", debug=False)
    for index in range(len(houseList)):
        basic = createBase("basics.txt", index, houseList[index])
        print(basic)
