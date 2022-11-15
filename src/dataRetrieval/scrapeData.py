from msilib.schema import Error
from bs4 import BeautifulSoup as bs
import requests
import numpy as np

"""I  find it weird that no listing (except for ONE) has ever been under 4.5 stars...
""" 
def get_page(city, state, country, n=1, debug=False):
    """ Scrape the first n*20 air bnb listings. 
    
        Args:
            city (str): City to search in
            state (str): State to search in
            country (str): Countr to search in
            n (int): Search for 20*n listings
            debug (Bolean): Enter Debug Mode
        
        Returns: 
            status (boolean): True if completed, false if errors
            all_prices (list): List of all prices
        
    """
    
    allPrices = []
    allRatings = []
    allBeds = []
    errors = 0

    # try:
    # Create base string
    city = city.replace(" ","-")
    country = country.replace(" ", "-")

    # Get 4 pages of info

    links = [f"http://airbnb.com/s/{city}--{state}--{country}/homes?tab_id=home_tab&" + \
                "refinement_paths%5B%5D=%2Fhomes&" + \
                f"flexible_trip_lengths%5B%5D=one_week&items_offset={20*(i+1)}&section_offset=3" 
                for i in range(n)]

    if debug:
        for l in links:
            print(f"Link: {l}")

    for l in links:

        res = requests.get(l)
        soup = bs(res.text, 'html.parser')

        # print("Parser setup complete\n")
        listings = soup.find_all("div", {"class": "c4mnd7m dir dir-ltr"})

        for l in listings:
            #Find price and separate it from dollar sign

            left = str(l.find_all("span", {"class": "a8jt5op dir dir-ltr"})[0]).split(" per")[0]
            price = int(left.split("$")[1])
            #taking out any commas if a house is in the thousands
            #if "," in priceString:
            #    priceString.replace(",", "")
            # price = int(priceString.split("$")[1])

            allPrices.append(price)
            
            #Find corresponding rating, separate it from html
            try:
                rating = str(l.find_all("span", {"class": "r1dxllyb dir dir-ltr"})[0]).split(" per")[0]
                # print(rating)
                ratingValue = str((rating.split("("))[0])
                # print(ratingValue)
                dataPos = ratingValue.rfind(">")+1
                ratingValue = ratingValue[dataPos:]
                # print(ratingValue)
                
                if str(ratingValue)[0] == "N":
                    ratingValue = "New"

            except IndexError:
                ratingValue = "New"

            allRatings.append(ratingValue)

            #Find amenities
            beds = (l.find_all(attrs={"class": "f15liw5s s1cjsi4j dir dir-ltr"}))
            bed = str(beds[1])
            bedValue = int(str((bed).split(">")[2])[0])

            allBeds.append(bedValue)

    return True, allPrices, allRatings, allBeds, errors
