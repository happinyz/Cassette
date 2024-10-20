from spotify import SpotifyClient
from capture import Camera

if __name__ == "__main__":
    sp = SpotifyClient()
    camera = Camera()
    query = camera.snap_and_process()
    track_id = sp.search(query)
    sp.play(track_id)
