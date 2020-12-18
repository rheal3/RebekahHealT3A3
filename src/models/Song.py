from main import db
from models.PlaylistSong import PlaylistSong
from sqlalchemy.orm import backref


class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False, unique=True)
    artist = db.Column(db.String(), nullable=False)

    # ??????!
    playlist = db.relationship("PlaylistSong", backref=backref("playlistsong.playlist_id", uselist=False))

    # lyrics_id = db.Column(db.Integer, db.ForeignKey("lyrics.id"), nullable=False)
    # audio_id = db.Column(db.Integer, db.ForeignKey("audio.id"), nullable=False)

    def __repr__(self):
        return f"<Song {self.title}>"
