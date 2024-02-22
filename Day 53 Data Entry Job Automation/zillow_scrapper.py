from bs4 import BeautifulSoup
import requests

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"


class ZillowBot:
    def __init__(self):
        url = ZILLOW_URL
        response = requests.get(url=url)
        zillow_webpage = response.text
        self.soup = BeautifulSoup(zillow_webpage, "html.parser")

    def scrap_data(self):
        properties = self.soup.find_all(name='li', class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        return properties

    def get_property_links(self):
        properties = self.scrap_data()
        property_links = []
        for property in properties:
            property_link = property.find("a").get("href")
            property_links.append(property_link)

        print(property_links)
        return property_links

    def get_property_adresses(self):
        properties = self.scrap_data()
        property_adresses = []
        for property in properties:
            property_address = property.find("a").getText().strip()
            property_adresses.append(property_address)

        print(property_adresses)
        return property_adresses

    def get_property_prices(self):
        properties = self.scrap_data()
        property_prices = []
        for property in properties:
            property_price = property.find(name='span',
                                           class_="PropertyCardWrapper__StyledPriceLine").getText().replace("+", "/")
            property_prices.append(property_price.split("/")[0])

        print(property_prices)
        return property_prices

# bot = ZillowBot()
# bot.get_property_prices()
# bot.get_property_adresses()
# bot.get_property_links()
