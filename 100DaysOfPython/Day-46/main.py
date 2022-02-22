from bs4 import BeautifulSoup
import lxml, requests
# base_url = "https://www.billboard.com/charts/hot-100/"
# user_date = "2005-03-15"#input("Which year do you  want to travel to ? Type the date in this format YYYY-MM-DD:")
# full_url = base_url+user_date
#
# response = requests.get(full_url)
# response.raise_for_status()
# soup = BeautifulSoup(response.text,"html.parser")
# print(soup)
# all_songs = []
# #all_song_tags = soup.find_all(name="li h3", id="title-of-a-story")#, class_="c-title ")
# all_song_tags = soup.find_all(name="h3")#, id="title-of-a-story",class_="c-title ")#select(selector="h3")
# for song_tag in all_song_tags:
#     all_songs.append(song_tag.getText())
#
# print(all_songs)


import requests
from bs4 import BeautifulSoup
url = "https://www.billboard.com/charts/hot-100/1965-06-25/"
date = "15-02-2015"#input('What date would you like to travel to? Type in YYYY-MM-DD format: ')
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
#print(soup)
#titles = soup.find_all(class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
titles = soup.find_all(name="h3")#, id="title-of-a-story")

titles_name = [title.getText() for title in titles]

print(titles_name)
# container = soup.find(name="div", class_="chart-results-list")
# titles = [song.getText() for song in container.find_all(name="h3", class_=["c-title", "a-no-trucate"], id="title-of-a-story")][2:]
# print(titles)
# print(len(titles))


# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
#
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
#                                                            client_secret="YOUR_APP_CLIENT_SECRET"))
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])