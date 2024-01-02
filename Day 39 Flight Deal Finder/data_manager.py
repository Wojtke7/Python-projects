import requests


class DataManager:
    sheet_url = "https://api.sheety.co/50ab9cbfa61830f47d54f41870031777/flightDeals/prices"

    def get_iatas(self):
        respond = requests.get(url=self.sheet_url)
        jsonRespond = respond.json()
        iatas = []

        for city in jsonRespond["prices"]:
            iatas.append(city["iataCode"])

        return iatas
