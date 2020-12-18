from main import ma
from models.Playlist import Playlist
from marshmallow.validate import Length
from schemas.SongSchema import SongSchema


class PlaylistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Playlist

    playlist_name = ma.String(required=True, validate=Length(min=1))
    songs = ma.Nested(SongSchema, many=True)

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)
