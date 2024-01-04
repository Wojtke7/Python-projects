from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager
flightData = FlightData()
New_flies = flightData.find_best_fly()
data_manager = DataManager()
sms_sender = NotificationManager()

new_ocassions_index = [index for index, element in enumerate(New_flies) if element is not None]
if not new_ocassions_index:
    print("Brak lepszych cen")
else:
    for index in new_ocassions_index:
        sms_sender.send_sms(New_flies[index])
        data_manager.change_prices(New_flies[index], index)


