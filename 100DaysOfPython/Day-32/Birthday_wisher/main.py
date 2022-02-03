##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas


def send_email(text, mail):
    my_email = "Test@gmail.com"
    password = "My_password"
    adders = mail

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=adders,
                            msg=f"Subject:Monday Motivation\n\n{text}.")

    print("The mail was sent ........")


df = pandas.read_csv("birthdays.csv")
data = df.to_dict(orient="records")

now = dt.datetime.now()
day = now.day
month = now.month

for user in data:
    if user["month"] == month and user["day"] == day:
        number = random.randint(1, 3)
        with open(f"letter_templates/letter_{number}.txt") as letter:
            contain = letter.read()
            mail_text = contain.replace("[NAME]", user["name"])
            mail = user["email"]
            print(f"Send mail to {mail}, with the next text\n{mail_text}")
            send_email(mail_text, mail)
