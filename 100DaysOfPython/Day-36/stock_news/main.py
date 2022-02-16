import requests, os
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "google"#"Tesla Inc"
STOCK_NAME = "F"
ARTICCLES = []
MESSAGE = []
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "BCUA2YZQI7X72VSY"

yesterday_closing_price= 0
day_before_yesterday_closing_price = 0
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key,

}

getnewsapi = "863025034cda43eaae57c5f43422a4ff"
parameters_2 = {
    "apiKey": getnewsapi,

}

def send_sms():
    global MESSAGE ,ARTICCLES

    account_sid = os.environ.get("OWM_API_KEY")
    auth_token = os.environ.get("token")

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"{MESSAGE}\n{ARTICCLES}",
        from_='+19034851279',
        to='+9720524879755'
        # to='+972523692124'
    )
    print(message.status)










#  6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#  7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
def get_news():
    global COMPANY_NAME, ARTICCLES
    response = requests.get("https://newsapi.org/v2/top-headlines/sources", params=parameters_2)
    response.raise_for_status()
    data = response.json()
    new_data = data["sources"]
    # print(new_data)
    for item in new_data:
        #print(item)
        if COMPANY_NAME in item["name"].lower():
            if len(ARTICCLES) < 3:
                ARTICCLES.append(item)
    print(ARTICCLES)


#  1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#  2. - Get the day before yesterday's closing stock price
def get_closing_prices():

    response = requests.get(url=STOCK_ENDPOINT, params=parameters)
    data = response.json()
    today = datetime.now()
    yesterday = datetime.now() - timedelta(1)

    stock_prices = data["Time Series (Daily)"]
    if 0 < today.weekday() <= 4:
        pass
    elif today.weekday() == 5:
        today = datetime.now() - timedelta(1)
    elif today.weekday() == 6:
        today = datetime.now() - timedelta(2)
    elif int(today.weekday()) == 0:
        today = datetime.now() - timedelta(2)

    yesterday = today - timedelta(1)
    day_before_yesterday= today - timedelta(2)

    for treading_day in stock_prices.items():
        global yesterday_closing_price , day_before_yesterday_closing_price
        type(treading_day[0])
        if treading_day[0] == str(yesterday.date()):
            yesterday_closing_price = treading_day[1]["4. close"]
            print(treading_day)
        if treading_day[0] == str(day_before_yesterday.date()):
            day_before_yesterday_closing_price = treading_day[1]["4. close"]
            print(treading_day)


#  3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#  4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#  5. - If TODO4 percentage is greater than 5 then print("Get News").
def calcult_delta():
    global yesterday_closing_price, day_before_yesterday_closing_price,MESSAGE ,STOCK_NAME
    increase = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    difference_in_price = float(increase) / float(yesterday_closing_price) * 100
    difference_in_price = '{0:.3g}'.format(difference_in_price)
    print(difference_in_price)
    if float(difference_in_price) > 5:
        text= f"{STOCK_NAME}:🔺{difference_in_price}%"
        MESSAGE.append(text)
        get_news()
    elif 5 or float(difference_in_price) < -5:
        text = f"{STOCK_NAME}:🔻{difference_in_price}%"
        MESSAGE.append(text)
        get_news()


get_closing_prices()
calcult_delta()
send_sms()

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

#  8. - Create a new list of the first 3 article's headline and description using list comprehension.

#  9. - Send each article as a separate message via Twilio.


# Optional : Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
