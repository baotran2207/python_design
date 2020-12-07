"""Default configuration

Use env var to override
"""
import os


ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND_URL")


# class Config(object):
#     ENV = os.getenv("FLASK_ENV")
#     DEBUG = ENV == "development"
#     SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     JWT_BLACKLIST_ENABLED = True
#     JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

#     ## os env
#     CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
#     CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND_URL")
# class DevConfig(Config):
#     pass



# class ProdConfig(Config):
#     pass
