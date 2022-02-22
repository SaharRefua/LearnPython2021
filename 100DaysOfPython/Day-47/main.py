import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.com/adidas-originals-snapback-flatbrim-Black/dp/B00U14RDBE/ref=sr_1_22?crid=24JUKBGA5ZVV1&keywords=hat+for+man&qid=1645530720&sprefix=hat+for+man%2Caps%2C340&sr=8-22"
TARGET_PRICE = 300

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language":  "en-US,en;q=0.9,he;q=0.8,he-IL;q=0.7",

}
def send_mail(deal_price,title):

    my_email = os.environ["my_mail"]
    password = os.environ["mail_password"]
    adders = "refua.sahar@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=adders,
                            msg=f"""Subject:Amazon deals \n\n{f"You must to checkout the new deal that i found in Amazon link:{title} "
                                                              f"{URL} in only : {deal_price}."}""")
    print("The mail was sent ........")





response = requests.get(url=URL , headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text,'html.parser')
spans= soup.findAll(name="span", class_="a-offscreen")
product_title=soup.find(id="productTitle")
prices = []
for span in spans:
    if "$" in span.getText():

        price = span.getText()
        prices.append(float(price.split("$")[1]))

print(prices)

if prices[1]<TARGET_PRICE:
    send_mail(prices[1],product_title.getText())
