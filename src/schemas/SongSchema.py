from main import ma
from models.Song import Song
from marshmallow.validate import Length
from schemas.AudioSchema import AudioSchema


class SongSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Song

    title = ma.String(required=True, validate=Length(min=1))
    artist = ma.String(required=True, validate=Length(min=1))
    audio = ma.Nested(AudioSchema)


song_schema = SongSchema()
songs_schema = SongSchema(many=True)
