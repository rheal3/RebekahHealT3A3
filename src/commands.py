from main import db
from flask import Blueprint


# Blueprint for flask db commands
db_commands = Blueprint("db-custom", __name__)


@db_commands.cli.command("create")
def create_db():
    """
    Custom flask db command to create all tables from models
    """

    db.create_all()
    print("TABLES CREATED")


@db_commands.cli.command("drop")
def drop_db():
    """
    Custome flask db command to drop all tables from database
    """

    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("TABLES DROPPED")


@db_commands.cli.command("seed")
def seed_db():
    """
    Custom flask db command to seed tables with fake data for testing
    """
    from models.User import User
    from models.Profile import Profile
    from models.Song import Song
    from models.Playlist import Playlist
    from models.Audio import Audio
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker()
    users = []

    # Create test users
    for i in range(5):
        user = User()
        user.email = f"test{i+1}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)

    # Create test admin user
    admin = User()
    admin.email = "admin@test.com"
    admin.password = bcrypt.generate_password_hash("123456").decode("utf-8")
    admin.admin = True
    db.session.add(admin)
    users.append(admin)

    db.session.commit()

    # Create test profile
    for i in range(5):
        profile = Profile()

        profile.username = f"User{i+1}"
        profile.firstname = faker.first_name()
        profile.lastname = faker.last_name()
        profile.user_id = users[i].id

        db.session.add(profile)

    # Create admin profile
    admin = Profile()
    admin.username = "admin"
    admin.firstname = "admin"
    admin.lastname = "admin"
    admin.user_id = users[-1].id
    db.session.add(admin)

    db.session.commit()


    # Create test playlist
    playlists = []
    for i in range(5):
        playlist = Playlist()
        playlist.playlist_name = f"Playlist{i+1}"
        db.session.add(playlist)
        playlists.append(playlist)

    db.session.commit()


    # Create test audio file
    audio_files = []
    for i in range(5):
        audio = Audio()
        audio.audio_file = f"./audiofiles/audio{i+1}"
        db.session.add(audio)
        audio_files.append(audio)
    
    db.session.commit()

    # Create test songs
    for i in range(5):
        playlist = random.choice(playlists)
        song =  Song()

        song.title = faker.catch_phrase()
        song.artist = faker.first_name()
        song.playlists.append(playlist)
        song.audio_id = audio_files[i].id

        db.session.add(song)
    
    db.session.commit()

        

    print("TABLES SEEDED")
