from main import db
# from models.PlaylistSong import playlists_songs
# from sqlalchemy.orm import backref


class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False, unique=True)
    artist = db.Column(db.String(), nullable=False)
    audio_id = db.Column(db.Integer, db.ForeignKey("audio.id"))

    # lyrics_id = db.Column(db.Integer, db.ForeignKey("lyrics.id"),
    #                       nullable=False)

    def __repr__(self):
        return f"<Song {self.title}>"
