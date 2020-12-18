from main import db
from models.PlaylistSong import playlists_songs
from sqlalchemy.orm import backref

class Playlist(db.Model):
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(), nullable=False, unique=True)
    songs = db.relationship("Song", secondary=playlists_songs, backref=backref("playlists", lazy="dynamic"))

    # connect to playlistsong join table which connects to song
    # ??????!


    def __repr__(self):
        return f"<Playlist {self.playlist_name}>"
