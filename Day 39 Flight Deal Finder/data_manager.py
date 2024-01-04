import requests


class DataManager:
    sheet_url = "https://api.sheety.co/50ab9cbfa61830f47d54f41870031777/flightDeals/prices"

    def get_iatas_and_prices(self):
        respond = requests.get(url=self.sheet_url)
        jsonRespond = respond.json()
        iatas = []
        prices = []

        for city in jsonRespond["prices"]:
            iatas.append(city["iataCode"])

        for price in jsonRespond["prices"]:
            prices.append(price["lowestPrice"])

        return iatas, prices

    def change_prices(self, dict, index):
        id = index + 2
        city = dict["dest_city"]
        price = dict["lowest_price"]
        sheet_endpoint = f"https://api.sheety.co/50ab9cbfa61830f47d54f41870031777/flightDeals/prices/{id}"
        header = {
            "Content-Type": "application/json"
        }
        body = {
            "price": {
               "lowestPrice": price
            }
        }
        respond = requests.put(url=sheet_endpoint, headers=header, json=body)
        print(respond.json())
