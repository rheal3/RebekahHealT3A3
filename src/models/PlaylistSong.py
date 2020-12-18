from main import db

playlists_songs = db.Table("playlists_songs", db.Model.metadata,
    db.Column("playlist_id", db.Integer, db.ForeignKey("playlists.id")),
    db.Column("song_id", db.Integer, db.ForeignKey("songs.id"))
)
