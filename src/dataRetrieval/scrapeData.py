# Uses an API to get the needed data

from msilib.schema import Error
from bs4 import BeautifulSoup as bs
import requests

def get_page(city, state, country, n=5, debug=False):
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
            # Should also find stay rankings for better analysis

            for l in listings:
                left = str(l.find_all("span", {"class": "a8jt5op dir dir-ltr"})[0]).split(" per")[0]
                price = int(left.split("$")[1])
                allPrices.append(price)

        return True, allPrices
    
    except:
        return False, allPrices
    