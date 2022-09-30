from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import createBase

if __name__ == "__main__":
    status, houseList, rating = get_page("Hillsboro", "Oregon", "US", debug=False)
    for index in range(len(houseList)-1):
        basic = createBase("basics.txt", 0, houseList[0], rating)
        print(basic)
