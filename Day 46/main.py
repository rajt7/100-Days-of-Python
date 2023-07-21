import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format:YYYY-MM-DD: ")

# Getting the top bollywood songs
response = requests.get(url=f"https://www.billboard.com/charts/india-songs-hotw/{date}/")
songs_webpage = response.text
soup = BeautifulSoup(songs_webpage, "html.parser")

top_songs = soup.find_all(name="h3", limit=25,
                          attrs={"id":  "title-of-a-story",
                                 "class": "a-no-trucate"})

all_songs = []
for song in top_songs:
    all_songs.append(song.getText().strip())

print(all_songs)

# Creating a scope and token for accessing spotipy library
scope = "playlist-modify-public"
username = os.environ['SPOTIFY_USERNAME']

token = SpotifyOAuth(scope=scope, username=username, redirect_uri="https://www.google.com/")
spotify_obj = spotipy.Spotify(auth_manager=token)

# Creating a playlist
spotify_obj.user_playlist_create(user=username, name=f"top 25 bollywood songs of {date}",
                                 public=True, description="Random...")
pre_playlist = spotify_obj.user_playlists(user=username)

# Getting the playlist id
playlist = pre_playlist['items'][0]['id']

# Searching the songs
songs_uri = []
for song in all_songs:
    result = spotify_obj.search(q=song, limit=2, market="IN")
    songs_uri.append(result['tracks']['items'][0]['uri'])

# Adding the songs to the playlist
spotify_obj.playlist_add_items(playlist_id=playlist, items=songs_uri)
