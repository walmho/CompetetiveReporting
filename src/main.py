from dataRetrieval.scrapeData import get_page

if __name__ == "__main__":
    status, houseList = get_page("Hillsboro", "Oregon", "US", debug=False)
