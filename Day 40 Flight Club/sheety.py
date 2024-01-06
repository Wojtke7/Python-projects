import requests

SHEET_ENDPOINT = "https://api.sheety.co/50ab9cbfa61830f47d54f41870031777/flightDeals/users"

header = {
    "Content-Type": "application/json"
}


def post_user(email, first_name, last_name):
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    respond = requests.post(url=SHEET_ENDPOINT, headers=header, json=body)
    print(respond.json())
