from zillow_scraper import ZillowScraper
from google_form_filler import GoogleFormFiller
import time

# Google Form Link: https://forms.gle/aohbYz9NgNFM6spTA

if __name__ == "__main__":
    zillow_scraper = ZillowScraper("https://appbrewery.github.io/Zillow-Clone/")
    listings_found = zillow_scraper.get_listings()

    google_form_filler = GoogleFormFiller("https://forms.gle/BpozLxbE7T9Ggun16")
    time.sleep(1)
    google_form_filler.enter_data_into_form(listings_found)
