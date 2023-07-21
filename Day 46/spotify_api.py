import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"
username = os.environ['SPOTIFY_USERNAME']

token = SpotifyOAuth(scope=scope, username=username, redirect_uri="https://www.google.com/")
spotify_obj = spotipy.Spotify(auth_manager=token)

# Creating a playlist
spotify_obj.user_playlist_create(user=username, name="random_playlist",
                                 public=True, description="Random...")
pre_playlist = spotify_obj.user_playlists(user=username)
print(pre_playlist)

# Getting the playlist id
playlist = pre_playlist['items'][0]['id']

song_uri = []
song_name = "Shree Hanuman Chalisa"
result = spotify_obj.search(q=song_name, limit=2, type='track', market="IN")
song_uri.append(result['tracks']['items'][0]['uri'])

spotify_obj.playlist_add_items(playlist_id=playlist, items=song_uri)
