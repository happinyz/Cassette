import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

class SpotifyClient:
    def __init__(self):
        self.client = None
        self.device_id = os.getenv('DEVICE_ID')
        self.authenticate()


    def authenticate(self):
        if self.client:
            print("already authenticated")
            return
        
        CLIENT_ID = os.getenv('CLIENT_ID')
        CLIENT_SECRET = os.getenv('CLIENT_SECRET')
        REDIRECT_URI = "http://localhost:8080"
        SCOPE = "user-read-playback-state,user-modify-playback-state"
        
        AUTH = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)

        self.client = spotipy.Spotify(auth_manager=AUTH)


    def play(self, track_id: str):
        self.authenticate()

        self.client.transfer_playback(device_id=self.device_id, force_play=False)

        # 5vNRhkKd0yEAg8suGBpjeY
        self.client.start_playback(device_id=self.device_id, uris=['spotify:track:' + track_id])


    def search(self, query: str):
        self.authenticate()

        results = self.client.search(q=query, type="track", limit=10)

        if not results:
            return None

        tracks = results["tracks"]["items"]
        if not len(tracks):
            return None
    
        # Get the track with the highest popularity
        track = max(tracks, key=lambda track: track['popularity'])

        print('Got track:', track["name"])
        return track["id"]
