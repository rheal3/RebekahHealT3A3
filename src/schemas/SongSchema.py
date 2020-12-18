from main import ma
from models.Song import Song
from marshmallow.validate import Length


class SongSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Song

    title = ma.String(required=True, validate=Length(min=1))
    artist = ma.String(required=True, validate=Length(min=1))


song_schema = SongSchema()
songs_schema = SongSchema(many=True)