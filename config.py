import os
import secret
basedir = os.path.abspath(os.path.dirname(__file__))

class Auth:
   CLIENT_ID = secret.CLIENT_ID
   CLIENT_SECRET = secret.CLIENT_SECRET
   AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
   TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
   USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
   

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI="postgresql://localhost/mac_app"


class TestingConfig(Config):
    TESTING = True
    
config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "default": DevelopmentConfig
}