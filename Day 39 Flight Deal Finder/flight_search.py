import json

import requests
from data_manager import DataManager
from datetime import datetime
from dateutil.relativedelta import relativedelta


class FlightSearch:
    POLAND_IATA = "KRK,KTW"
    flight_url = "https://api.tequila.kiwi.com/v2/search"

    def search_flights(self):
        today_date = datetime.now().strftime("%d/%m/%Y")
        six_month_later = datetime.now() + relativedelta(months=5)
        # print(six_month_later.strftime("%d/%m/%Y"))

        data_manager_instance = DataManager()
        destinations, prices = data_manager_instance.get_iatas_and_prices()
        responds = []

        flight_header = {
            "apikey": "LgKc60UiKJFmzRjXid63dTu5xpABqtz7",
            "Content-Type": "application/json",
            "Content-Encoding": "gzip"
        }

        for destination, price in zip(destinations, prices):
            body = {
                "fly_from": self.POLAND_IATA,
                "fly_to": destination,
                "date_from": today_date,
                "date_to": six_month_later.strftime("%d/%m/%Y"),
                "curr": "EUR",
                "price_to": price,
                "max_stopovers": "0",
                "nights_in_dst_from": "2",
                "nights_in_dst_to": "14"
            }

            respond = requests.get(url=self.flight_url, headers=flight_header, params=body)
            data = respond.json()
            json_respond = json.dumps(respond.json())
            # print(data)
            # print(json_respond)

            if data["_results"] != 0 and data["data"][0]["price"] < price:
                print(data["data"][0])
                responds.append(data["data"][0])
            elif data["_results"] == 0:
                print(f"Nie znaleziono bezpośredniego lotu do {destination}, szukanie z przesiadką")
                body["max_stopovers"] = "2"
                respond2 = requests.get(url=self.flight_url, headers=flight_header, params=body)
                data2 = respond2.json()

                #Znaleziono z przesiadką i cena niższa
                if data2["_results"] != 0 and data2["data"][0]["price"] < price:
                    print(f"Znaleziono lot do {destination} z przesiadką!")
                    print(data2["data"][0])
                    responds.append(data2["data"][0])
                else:
                    print(f"Nie znaleziono lotu z jedną przesiadką, brak lotów do {destination} lub za wysoka cena")
                    responds.append(None)

            else:
                print(f"Znaleziono bezpośredni lot do {destination}, ale cena nie była korzystniejsza")
                responds.append(None)

        return responds


flightSearch = FlightSearch()
flightSearch.search_flights()

# print(destinations)
# print(prices)
# today_date = datetime.now().strftime("%d/%m/%Y")
# six_month_later = datetime.now() + relativedelta(months=5)
# print(six_month_later.strftime("%d/%m/%Y"))
