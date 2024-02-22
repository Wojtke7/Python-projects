from zillow_scrapper import ZillowBot
from forms_bot import FormsBot

zillow_bot = ZillowBot()
forms_bot = FormsBot()

addresses = zillow_bot.get_property_adresses()
links = zillow_bot.get_property_links()
prices = zillow_bot.get_property_prices()

forms_bot.fill_form(addresses, prices, links)
