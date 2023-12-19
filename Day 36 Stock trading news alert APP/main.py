import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

#setting date
today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

account_sid = 'AC6674645ca792857c7c35c7f413c96414'
auth_token = '8825fedf8c99befdc5e11c9130a4d2ae'
client = Client(account_sid, auth_token)

#static variables
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK_KEY = "1G9K3UZNE79RJAOH"
API_NEWS_KEY = "8fcf861a67194935bbcefe1f26c7b295"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#collecting stock data
stock_url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_STOCK_KEY}'
r = requests.get(stock_url)
stock_data = r.json()

#collecting news data
news_url = f"{NEWS_ENDPOINT}?q={COMPANY_NAME}&from=2023-11-19&language=en&sortBy=publishedAt&apiKey={API_NEWS_KEY}"
re = requests.get(news_url)
news_data = re.json()

#collecting prices
try:
    yesterday_close_price = stock_data["Time Series (Daily)"][yesterday.strftime("%Y-%m-%d")]["4. close"]
    day_before_close_price = stock_data["Time Series (Daily)"][day_before_yesterday.strftime("%Y-%m-%d")]["4. close"]
except KeyError:
    quit()

percentage_diff = round(((yesterday_close_price - day_before_close_price) / yesterday_close_price) * 100, 2)
print(percentage_diff)

#sending alerts
if percentage_diff > 5 or percentage_diff < -5:
    emoji = "🔺" if percentage_diff > 5 else "🔻"

    for i in range(3):
        headline = news_data["articles"][i]["title"]
        brief = news_data["articles"][i]["description"]

        message = client.messages.create(
            from_='+12058596307',
            body=f'{STOCK_NAME}: {emoji}{percentage_diff}%\n'
                 f'Headline: {headline}\n'
                 f'Brief: {brief}',
            to='+48572315551'
        )

        print(message.sid)
