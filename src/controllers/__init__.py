from controllers.auth_controller import auth
from controllers.profile_controller import profiles
from controllers.songs_controller import songs
from controllers.playlist_controller import playlists

registerable_controllers = [
    auth,
    profiles,
    songs,
    playlists
    ]
