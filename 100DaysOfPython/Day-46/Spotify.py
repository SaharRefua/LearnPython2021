
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
#                                                            client_secret="YOUR_APP_CLIENT_SECRET"))
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None