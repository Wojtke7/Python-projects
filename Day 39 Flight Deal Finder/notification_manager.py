from twilio.rest import Client

class NotificationManager:
    account_sid = 'AC6674645ca792857c7c35c7f413c96414'
    auth_token = 'SECRET TOKEN'
    client = Client(account_sid, auth_token)

    def send_sms(self, dict):
        if dict["stepover_city"] is None:
            message = self.client.messages.create(
                from_='+12058596307',
                body=f'Low price alert! Only {dict["lowest_price"]}€ to fly from {dict["dep_city"]}-{dict["dep_IATA"]} to {dict["dest_city"]}-{dict["dest_IATA"]}, from {dict["dep_date"]} to {dict["back_date"]}.\n',
                to='+48572315551'
            )
            print(message.sid)
        else:
            message = self.client.messages.create(
                from_='+12058596307',
                body=f'Low price alert! Only {dict["lowest_price"]}€ to fly from {dict["dep_city"]}-{dict["dep_IATA"]} to {dict["dest_city"]}-{dict["dest_IATA"]}, from {dict["dep_date"]} to {dict["back_date"]}.\n'
                     f'Flight has 1 stop over, via {dict["stepover_city"]}-{dict["stepover_IATA"]}',
                to='+48572315551'
            )
            print(message.sid)
