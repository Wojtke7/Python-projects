from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager

flightData = FlightData()
New_flights = flightData.find_best_fly()
data_manager = DataManager()
notification_sender = NotificationManager()

new_ocassions_index = [index for index, element in enumerate(New_flights) if element is not None]
if not new_ocassions_index:
    print("Brak lepszych cen")
else:
    for index in new_ocassions_index:
        notification_sender.send_sms(New_flights[index])
        notification_sender.send_emails(New_flights[index])
        data_manager.change_prices(New_flights[index], index)



