from main import db
from flask import Blueprint


# Blueprint for flask db commands
db_commands = Blueprint("db", __name__)


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
    from main import bcrypt
    from faker import Faker

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

    db.session.commit()

    # Create test profile
    for i in range(5):
        profile = Profile()

        profile.username = faker.first_name()
        profile.firstname = faker.first_name()
        profile.lastname = faker.last_name()
        profile.user_id = users[i].id

        db.session.add(profile)

    db.session.commit()

    print("TABLES SEEDED")
