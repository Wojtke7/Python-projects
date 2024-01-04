from twilio.rest import Client


class NotificationManager:
    account_sid = 'AC6674645ca792857c7c35c7f413c96414'
    auth_token = '6e8adcacb5a3182c3a7d73bc94da6299'
    client = Client(account_sid, auth_token)

    def send_sms(self, dict):
        message = self.client.messages.create(
            from_='+12058596307',
            body=f'Low price alert! Only {dict["lowest_price"]}€ to fly from {dict["dep_city"]}-{dict["dep_IATA"]} to {dict["dest_city"]}-{dict["dest_IATA"]}, from {dict["dep_date"]} to {dict["back_date"]}.\n',
            to='+48572315551'
        )
        print(message.sid)
