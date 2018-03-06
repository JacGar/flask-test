import os.path

class Config(object):
    """
    Common configurations
    """

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+db_path
    FLASK_CONFIG = "development"
    FLASK_APP = "run.py"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = b"powerful secretkey"
    WTF_CSRF_SECRET_KEY = b'a csrf secret key'


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}