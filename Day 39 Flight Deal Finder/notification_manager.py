import smtplib
from data_manager import DataManager

from twilio.rest import Client


class NotificationManager:
    account_sid = 'AC6674645ca792857c7c35c7f413c96414'
    auth_token = 'SECRET_TOKEN'
    client = Client(account_sid, auth_token)

    sending_mail = "wojciechmarcela7@gmail.com"
    sending_password = "rxttlfneryuuujiw"

    def send_sms(self, dict):

        if dict["stepover_city"] is None:
            stopover_info = ""
        else:
            stopover_info = "Flight has 1 stop over, via " + dict["stepover_city"] + "-" + dict["stepover_IATA"]

        message = self.client.messages.create(
            from_='+12058596307',
            body=f'Low price alert! Only {dict["lowest_price"]}€ to fly from {dict["dep_city"]}-{dict["dep_IATA"]} to {dict["dest_city"]}-{dict["dest_IATA"]}, from {dict["dep_date"]} to {dict["back_date"]}.\n {stopover_info}',
            to='+48572315551'
        )
        print(message.sid)

    def send_emails(self, dict):
        data_manager = DataManager()
        users = data_manager.get_users()

        if dict["stepover_city"] is None:
            stopover_info = ""
        else:
            stopover_info = "Flight has 1 stop over, via " + dict["stepover_city"] + "-" + dict["stepover_IATA"]

        for user in users["users"]:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.sending_mail,
                                 password=self.sending_password)
                connection.sendmail(from_addr=self.sending_mail, to_addrs=user["email"],
                                    msg=f'Low price alert! Only {dict["lowest_price"]}€ to fly from {dict["dep_city"]}-{dict["dep_IATA"]} to {dict["dest_city"]}-{dict["dest_IATA"]}, from {dict["dep_date"]} to {dict["back_date"]}.\n {stopover_info}'.encode('utf-8'))
