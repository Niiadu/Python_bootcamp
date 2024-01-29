import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

"31pl6pn4byfg3buf2sej6izublaa"
CLIENT_ID = "dda00a270ec54f66bb20bb5173673d86"
CLIENT_SECRET = "0b04e7a4724b4f78ab9bb63b191e2e84"
musical_year = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/2021-10-10"

response = requests.get(billboard_url)
billboard_data = response.text

soup = BeautifulSoup(billboard_data, "html.parser")
hot_100 = soup.select("li ul li h3")
music = [music.getText().strip() for music in hot_100]
print(music)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Nii Adu"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = musical_year.split("-")[0]
for song in music:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")


playlist = sp.user_playlist_create(user=user_id, name=f"{musical_year} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)