from main import db

class PlaylistSong(db.Model):
    __tablename__ = "playlistsong"

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    # connect to playlistsong join table which connects to song

    def __repr__(self):
        return f"<Playlist {self.playlist_name}>"