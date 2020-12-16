import os


# overall basic config settings
class Config(object):
    # turn off modification tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "scatter"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # database uri to connect to
        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set.")

        return value


# specific settings for dev env
class DevelopmentConfig(Config):
    DEBUG = True


# specific settings for production env
class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_SECRET_KEY")

        if not value:
            raise ValueError("JWT Secret Key is not set.")

        return value


# specific settings for testing env
class TestingConfig(Config):
    TESTING = True


# gets current environment flask is set to
environment = os.environ.get("FLASK_ENV")

# sets app_config based on environment
if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
