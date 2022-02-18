from bs4 import BeautifulSoup
import lxml

with open("website.html", "r", encoding='utf-8') as html_file:
    contents = html_file.read()
#print(contents)

soup = BeautifulSoup(contents,"html.parser")
#print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

for tag in  all_anchor_tags:
    #print(tag.getText()) # Get the text of a tag
    print(tag.get("href")) #get the value hyper link


heading = soup.find(name="h1",id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

# select one will return the first
company_url = soup.select_one(selector="p a")
print(company_url)

# select return all the tag that his find
h3_heading = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name")
print(name)
heading = soup.select_one(".heading")
print(heading)


