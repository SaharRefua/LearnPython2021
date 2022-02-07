import requests
import datetime
import os
from twilio.rest import Client

account_sid = os.environ.get("OWM_API_KEY")
auth_token = os.environ.get("token")
STOCK = "TSLA"
# STOCK = "APPEL"
# STOCK = "BBC"
COMPANY_NAME = "Tesla Inc"
COMPANY_NAME = "Appel"
COMPANY_NAME = "Google"
api_key = "BCUA2YZQI7X72VSY"
message = ""

parameters = {

    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    # "slice":"day1",
    # "slice":"year1month1",
    # "outputsize":"full",
    "apikey": api_key,

}
newsapi = "863025034cda43eaae57c5f43422a4ff"
parameters_2 = {
    "apiKey": newsapi,

}


def send_sms(auth_token, account_sid, message):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{message}.",
        from_='+19034851279',
        to='+9720524879755'
        # to='+972523692124'
    )
    print(message.status)


date = datetime.datetime.now()
def get_stock_price(parameters):
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()
    hour_for_each_day = data["Time Series (60min)"]
    return hour_for_each_day

def get_last_trading_date(date_):
    if 0 <= date_.weekday() <= 4:
        # print("during trading days")
        stock_prices=get_stock_price(parameters)

    else:
        # day = str(date_)
        day = date_.day
        day = int(day) - 1
        date_ = date_.replace(day=day)
        print(date_)
        get_last_trading_date(date_)


# print(date.date())

trading_date = get_last_trading_date(date)
print(trading_date)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    # print(hour_for_each_day)
    #
    # for hour in hour_for_each_day.items():
    #     date_time = str(hour[0])
    #     new_date = date_time.split(" ")[0]
    #     print(new_date, trading_date)
    #     if new_date == str(trading_date.date()):
    #         print("good")


# print(hour[0])


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(parameters_2, COMPANY_NAME):
    response = requests.get("https://newsapi.org/v2/top-headlines/sources", params=parameters_2)
    response.raise_for_status()
    data = response.json()
    new_data = data["sources"]
    # print(new_data)
    for item in new_data:
        if COMPANY_NAME == item["name"]:
            print(item)
    # message += f"{STOCK}: 🔺 @%\n"


# get_news(parameters_2, COMPANY_NAME)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

# send_sms(auth_token,account_sid, message)
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
