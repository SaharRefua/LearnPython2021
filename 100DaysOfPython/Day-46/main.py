from bs4 import BeautifulSoup
import lxml, requests
base_url = "https://www.billboard.com/charts/hot-100/"
user_date = "2005-03-15"#input("Which year do you  want to travel to ? Type the date in this format YYYY-MM-DD:")
full_url = base_url+user_date

response = requests.get(full_url)
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")
print(soup)
all_songs = []
#all_song_tags = soup.find_all(name="li h3", id="title-of-a-story")#, class_="c-title ")
all_song_tags = soup.select(selector="h3")
for song_tag in all_song_tags:
    all_songs.append(song_tag.getText())

print(all_songs)

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