"""Default configuration

Use env var to override
"""
import os


class Config(object):
    DEBUG = ENV == "development"
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]


    ## os env 
    ENV = os.getenv("FLASK_ENV")
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND_URL")
class DevConfig(Config):
    pass


class TestConfig(Config):
    SECRET_KEY=testing
    DATABASE_URI='postgresql://dise:passw0rD!@95.216.114.137:5432/baotran_test'
    CELERY_BROKER_URL='redis://95.216.114.137:6380/0'
    CELERY_RESULT_BACKEND_URL='redis://95.216.114.137:6380/0'

class ProdConfig(Config):
    pass
