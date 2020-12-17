from main import db

class Playlist(db.Model):
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(), nullable=False, unique=True)
    # connect to playlistsong join table which connects to song

    def __repr__(self):
        return f"<Playlist {self.playlist_name}>"
