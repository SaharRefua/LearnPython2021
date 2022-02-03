import smtplib
import datetime as dt
import random


def get_quote():
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)
        return quote


def send_email():
    quote = get_quote()
    my_email = "Test@gmail.com"
    password = "My_password"
    adders = "Test@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=adders,
                            msg=f"Subject:Monday Motivation\n\n{quote}.")

    print("The mail was sent ........")


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:
    send_email()

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(now)
# print(year)
# print(day_of_week )
# date_of_birth = dt.datetime(year=1995, month=12 , day=15)
# print(date_of_birth)
# date_of_birth = dt.datetime(year=1995, month=12 , day=15, hour=8)
# print(date_of_birth)


# def send_email():
#     quote = get_quote()
#     my_email = "Test@gmail.com"
#     password = "My_Password"
#     adders = "Test@gmail.com"
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()  # secure the connection
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs=adders,
#                             msg="Subject:Hello Sahar\n\nThis is the body of my email.")
#
#     print("The mail was sent ........")
