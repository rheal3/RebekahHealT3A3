from main import db
from models.Song import Song
from sqlalchemy.orm import backref


class Lyrics(db.Model):
    __tablename__ = "lyrics"

    id = db.Column(db.Integer, primary_key=True)
    lyrics_file = db.Column(db.String(), nullable=False, unique=True)
    # song = db.relationship("Song", backref=backref("lyrics_file", uselist=False))

    def __repr__(self):
        return f"<Lyrics File Location {self.lyrics_file}>"
