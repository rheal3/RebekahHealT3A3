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


# view single playlist
@playlists.route("/<int:id>", methods=["GET"])
def playlist_show(id):
    playlist = Playlist.query.get(id)
    return jsonify(playlist_schema.dump(playlist))


# add song to playlist
@playlists.route("/<int:id>/song", methods=["POST"])
def playlist_add_song(id):
    # playlist = Playlist.query.get(id)

    # playlist.song = ???
    pass


# remove song from playlist
@playlists.route("/<int:id>/song", methods=["DELETE"])
def playlist_delete_song(id):
    pass


# edit playlist
@playlists.route("/<int:id>", methods=["PUT", "PATCH"])
def playlist_update(id):
    pass


# remove playlist
@playlists.route("/<int:id>", methods=["DELETE"])
def playlist_delete(id):
    pass
