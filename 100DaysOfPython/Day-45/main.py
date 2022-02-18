from bs4 import BeautifulSoup
import lxml, requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")
#print(soup)


article_tag = soup.find(class_="titlelink" , name="a")
article_text = article_tag.getText()
article_link = article_tag.get("href")

print(article_tag)
print(article_text)
print(article_link)

score = soup.find(class_="score" , name="span")
article_upovte = score.getText()

print(article_upovte)

# all_anchor_tage = soup.find_all(class_="titlelink" , name="a")
# for tag in all_anchor_tage:
#     print(tag.getText())