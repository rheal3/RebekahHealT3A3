from models.Playlist import Playlist
from schemas.PlaylistSchema import playlist_schema, playlists_schema
from main import db
# from services.auth_service import verify_user
# from sqlalchemy.orm import joinedload
# from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify, abort


playlists = Blueprint("playlists", __name__, url_prefix="/playlist")


@playlists.route("/", methods=["GET"])
def playlist_index():
    playlists = Playlist.query.all()
    return jsonify(playlists_schema.dump(playlists))

@playlists.route("/", methods=["POST"])
def playlist_create():
    playlist_fields = playlist_schema.load(request.json)

    new_playlist = Playlist()
    new_playlist.playlist_name = playlist_fields["playlist_name"]

    db.session.add(new_playlist)
    db.session.commit()

    return jsonify(playlist_schema.dump(new_playlist))


# create playlist
# add playlist to playlist
# remove playlist from playlist
# edit playlist
# remove playlist