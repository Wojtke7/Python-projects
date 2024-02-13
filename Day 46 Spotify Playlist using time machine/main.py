from bs4 import BeautifulSoup
import requests
import spotify

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

if response.status_code != 200:
    print("An error occurred. Please check your input and try again.")


songs_webpage = response.text
soup = BeautifulSoup(songs_webpage, "html.parser")

song_names_spans = soup.select("li ul li h3")

# print(song_names_spans)
song_names = []

for song in song_names_spans:
    song_names.append(song.getText().strip())


track_list = spotify.create_song_list(song_names, date.split("-")[0])
spotify.create_playlist(date, track_list)
