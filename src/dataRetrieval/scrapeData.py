from msilib.schema import Error
from bs4 import BeautifulSoup as bs
import requests

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
    
    try:
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

            listings = soup.find_all("div", {"class": "c4mnd7m dir dir-ltr"})

            for l in listings:
                #Find price and separate it from dollar sign
                left = str(l.find_all("span", {"class": "a8jt5op dir dir-ltr"})[0]).split(" per")[0]
                price = int(left.split("$")[1])
                #taking out any commas if a house is in the thousands
                allPrices.append(price)
                
                #Find corresponding rating, separate it from html
                rating = str(l.find_all("span", {"class": "r1dxllyb dir dir-ltr"})[0]).split(" per")[0]
                ratingValue = str((rating.split(">")[1]).split("(")[0])

                #Defaulting new listings without any ratings to a string value. May want to consider removing corresponding houses
                if ratingValue[0] == "N":
                    ratingValue = "New"
                allRatings.append(ratingValue)

        return True, allPrices, allRatings
    
    except Exception as e:
        # print(f"{len(allPrices)}\n\n{allPrices}")
        # print(f"{len(allRatings)}\n\n{allRatings}")
        print(e)
        return False, allPrices, allRatings
    