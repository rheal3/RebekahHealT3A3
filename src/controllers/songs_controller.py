from models.Song import Song
from models.User import User
from schemas.SongSchema import song_schema, songs_schema
from main import db
# from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

songs = Blueprint("songs", __name__, url_prefix="/songs")

@songs.route("/", methods=["GET"])
def songs_index():
    # lyrics = Lyrics.query.options(joinedload("lyrics")).all()
    # audio = Audio.query.options(joinedload("audio")).all()
    # songs = Song.query.options(joinedload("songs")).all()
    songs = Song.query.all()
    return jsonify(songs_schema.dump(songs))

@songs.route("/", methods=["POST"])
def song_create():

    song_fields = song_schema.load(request.json)

    # admin = User.query.get(get_jwt_identity())

    # if not admin.admin:
    #     return abort(401, description="Invalid user action.")

    new_song = Song()
    new_song.title = song_fields["title"]
    new_song.artist = song_fields["artist"]

    db.session.add(new_song)
    db.session.commit()

    return jsonify(song_schema.dump(new_song))

@songs.route("/<int:id>", methods=["GET"])
def song_show(id):
    song = Song.query.get(id)
    return jsonify(song_schema.dump(song))

@songs.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
# @verify_user
def song_update(id):

    song_fields = song_schema.load(request.json)
    song = Song.query.filter_by(id=id)
    if not song:
        return abort(401, description="Unauthorized action.")

    song.update(song_fields)
    db.session.commit()
    return jsonify(song_schema.dump(song[0]))

