from dataRetrieval.scrapeData import get_page
import matplotlib.pyplot as plt

if __name__ == "__main__":
    status, houseList, rating = get_page("Hillsboro", "Oregon", "US", debug=False)
    priceVsRating = {houseList[i]: rating[i] for i in range(len(houseList))}
    
    plt.bar(rating, houseList)
    plt.show()
