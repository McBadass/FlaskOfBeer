import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secrets'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DB_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://postgres:bathersxPcWtYa39HqgQMNyt5Y3@192.168.1.103:5432/FOBDev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DB_URI = os.environ.get('TEST_DATABASE_URL') or \
        'postgresql://postgres:bathersxPcWtYa39HqgQMNyt5Y3@192.168.1.103:5432/FOBTest'
    # Not sure if this is needed below
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DB_URI = os.environ.get('PROD_DATABASE_URL') or \
        'postgresql://postgres:bathersxPcWtYa39HqgQMNyt5Y3@192.168.1.103:5432/FOBProd'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
