from bs4 import BeautifulSoup
import requests


class ZillowScraper:
    def __init__(self, url):
        html = requests.get(url).text
        self.soup = BeautifulSoup(html, 'html.parser')
        self._listings = []

    def __cleanup_prices(self, price):
        """Removes unnecessary symbols and text from the price data"""
        return price[:price.index('+')] if '+' in price else price[:price.index('/')]

    def __cleanup_addresses(self, address):
        """Removes unnecessary whitespace, newlines, and pipes from the address data"""
        return address.replace(' | ', ' ')

    def __update_listings(self):
        """Get the Zillow listings results from the results page.
        Returns a list of dictionaries containing data of each listing"""
        urls = [
            item.get('href') for item in
            self.soup.select("#grid-search-results ul li div div article div div a.StyledPropertyCardDataArea-anchor")
        ]
        prices = [
            self.__cleanup_prices(item.get_text()) for item in
            self.soup.select("#grid-search-results ul li div div article div div div div span")
        ]
        addresses = [
            self.__cleanup_addresses(item.get_text().strip()) for item in
            self.soup.select("#grid-search-results ul li div div article div div a address")
        ]
        for listing in zip(urls, prices, addresses):
            self._listings.append(
                {
                    "url": listing[0],
                    "price": listing[1],
                    "address": listing[2]
                }
            )

    def get_listings(self) -> list:
        """Returns the updated set of listings on Zillow."""
        self.__update_listings()
        return self._listings
