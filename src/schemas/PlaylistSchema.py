from main import ma
from models.Playlist import Playlist
from marshmallow.validate import Length


class PlaylistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Playlist

    playlist_name = ma.String(required=True, validate=Length(min=1))
    songs = ma.List()
    # songplaylist join table??

    # have nested songs in here

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)
