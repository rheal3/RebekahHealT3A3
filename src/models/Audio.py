from main import db
from models.Song import Song
from sqlalchemy.orm import backref


class Audio(db.Model):
    __tablename__ = "audio"

    id = db.Column(db.Integer, primary_key=True)
    audio_file = db.Column(db.String(), nullable=False, unique=True)
    song = db.relationship("Song", backref=backref("audio_file", uselist=False))


    def __repr__(self):
        return f"<Audio File Location {self.audio_file}>"
