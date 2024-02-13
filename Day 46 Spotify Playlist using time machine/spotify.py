import spotipy.oauth2

CLIENT_ID = "d45a4841cd4244bf8c46818e9d368576"
CLIENT_SECRET = "CLIENT_SECRET"
REDIRECT_URI = "http://example.com"


def auth():
    sp = spotipy.Spotify(
        auth_manager=spotipy.oauth2.SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope="playlist-modify-private",
            show_dialog=True,
            cache_path="token.txt",
            username="Wojtek Marcela"
        )
    )

    user_id = sp.current_user()["id"]

    return user_id, sp


def create_song_list(song_names, year):
    authentications = auth()
    track_list = []

    for name in song_names:
        track = authentications[1].search(q=f"track: {name} year: {year}", limit=1, type="track")
        # print(track)
        try:
            track_list.append(track["tracks"]["items"][0]["uri"])
        except IndexError:
            pass
    print(track_list)
    print(len(track_list))

    return track_list


def create_playlist(date, track_list):
    authentications = auth()
    sp = authentications[1]
    user_id = authentications[0]

    playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

    print(type(track_list))
    print(playlist_id)
    print(type(playlist_id))

    sp.playlist_add_items(playlist_id=playlist_id["id"], items=track_list)
