import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text,"html.parser")

all_h3 = soup.find_all(name="h3", class_="title")
all_movies = []
for movie in all_h3:
    all_movies.append( movie.getText())
print(all_movies)
# movies = all_movies[::-1]
with open("movies.txt", "w") as file:

    for n in range(len(all_movies)-1, -1, -1):
         file.write(f"{all_movies[n]}\n")
