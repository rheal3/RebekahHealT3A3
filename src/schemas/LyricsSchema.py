from main import ma
from models.Lyrics import Lyrics
from marshmallow.validate import Length


class LyricsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lyrics
    
    # validate by checking file exists???
    lyrics_file = ma.String(required=True, validate=Length(min=4))

lyric_schema = LyricsSchema()
lyrics_schema = LyricsSchema(many=True)

