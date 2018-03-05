class Config(object):
    """
    Common configurations
    """

    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    FLASK_CONFIG = "development"
    FLASK_APP = "run.py"

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