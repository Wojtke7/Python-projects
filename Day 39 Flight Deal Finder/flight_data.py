from flight_search import FlightSearch
from datetime import datetime, timedelta


class FlightData:
    flightSearch = FlightSearch()
    # List of json obejcts
    data = flightSearch.search_flights()

    def find_best_fly(self):
        flies = []

        for fly in self.data:
            if fly is not None:
                dep_city = fly["cityFrom"]
                dest_city = fly["cityTo"]

                dep_date = fly["local_departure"].split("T")[0]
                days = fly["nightsInDest"]
                date = datetime.strptime(dep_date, '%Y-%m-%d')
                back_date = (date + timedelta(days=days)).strftime("%Y-%m-%d")
                print(dep_date)
                print(back_date)

                print(f"Flight from {dep_city} to {dest_city} changed")

                dict = {
                    "lowest_price": fly["price"],
                    "dep_IATA": fly["flyFrom"],
                    "dest_IATA": fly["flyTo"],
                    "dep_city": fly["cityFrom"],
                    "dest_city": fly["cityTo"],
                    "dep_date": dep_date,
                    "back_date": back_date
                }

                flies.append(dict)
            else:
                flies.append(None)

        # print(flies)
        return flies
