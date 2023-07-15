import requests
from twilio.rest import Client

MY_LAT = 50.184820
MY_LONG = 19.482790

account_sid = 'AC6674645ca792857c7c35c7f413c96414'
auth_token = 'b0535a3f67b4d483675760025a90a198'


def check_showers_hourly(weathercode):
    drizzle_hours = []
    rain_hours = []
    heavy_rain_hours = []
    snow_hours = []
    thunderstorm_hours = []

    for hour_code in weathercode:
        if 50 < hour_code < 60:
            drizzle_hours.append(weathercode.index(hour_code) + 8)
        elif 60 < hour_code < 70:
            rain_hours.append(weathercode.index(hour_code) + 8)
        elif 70 < hour_code < 80 or 85 <= hour_code < 87:
            snow_hours.append(weathercode.index(hour_code) + 8)
        elif 80 < hour_code < 85:
            heavy_rain_hours.append(weathercode.index(hour_code) + 8)
        elif 94 < hour_code < 100:
            thunderstorm_hours.append(weathercode.index(hour_code) + 8)

    statement = ""

    if drizzle_hours:
        drizzle_str = ', '.join(map(str, drizzle_hours))
        statement += f"Mżawka przewidywana jest w godzinach: {drizzle_str}"

    if rain_hours:
        rain_str = ', '.join(map(str, rain_hours))
        statement += f"Deszcz przewidywany jest w godzinach: {rain_str}"

    if heavy_rain_hours:
        heavy_rain_str = ', '.join(map(str, heavy_rain_hours))
        statement += f"Mocny deszcz przewidywany jest w godzinach: {heavy_rain_str}"

    if snow_hours:
        snow_str = ', '.join(map(str, snow_hours))
        statement += f"Śnieg przewidywany jest w godzinach: {snow_str}"

    if thunderstorm_hours:
        thunderstorm_str = ', '.join(map(str, thunderstorm_hours))
        statement += f"Burza przewidywana jest w godzinach: {thunderstorm_str}"

    return statement


response = requests.get(
    url="https://api.open-meteo.com/v1/forecast?latitude=50.19&longitude=19.48&hourly=weathercode&daily=weathercode&forecast_days=1&timezone=Europe%2FBerlin")
response.raise_for_status()
data = response.json()

# Explanation https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c
# We are checking the weathercode between 8 AM and 10 PM
weathercode = data["hourly"]["weathercode"][8:22]
print(weathercode)

will_rain = False

# Everything which is higher than 50 in weather code is rain or snow
for code in weathercode:
    if code > 50:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Dzisiaj będzie padać ☂️.",
        from_='+14066686800',
        to='+48572315551'
    )
    print(message.status)

else:
    print("Today without rain!")
