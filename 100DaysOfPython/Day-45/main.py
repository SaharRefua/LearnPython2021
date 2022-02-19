from bs4 import BeautifulSoup
import lxml, requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")
#print(soup)

#
# article_tag = soup.find(class_="titlelink" , name="a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
#
# print(article_tag)
# print(article_text)
# print(article_link)
#
# score = soup.find(class_="score" , name="span")
# article_upovte = score.getText()
#
# print(article_upovte)
article_texts = []
article_links = []
articles = soup.find_all(class_="titlelink" , name="a")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_number = max(article_upvotes)
index = article_upvotes.index(max_number)



link = article_links[index]
text = article_texts[index]



print(f"max number of upvotes is : {max_number} \nthe article text: {text} \nthe article link: {link}" )

