import os
from data_manager import DataManager

class FlightSearch:
    POLAND_IATA = "KRK,KTW"
    flight_url = "https://api.tequila.kiwi.com/v2/search"

    data_manager_instance = DataManager()
    iatas_string = ','.join(data_manager_instance.get_iatas())

    flight_header = {
        "apikey": os.environ["API_KEY"]
    }

    body_header = {
        "fly_from": POLAND_IATA,

    }

