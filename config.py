from app.utils.aws_utils import get_secret
from constants import AWS_SECRET, AWS_REGION
from os import environ
import logging

log = logging.getLogger()
class ProdConfig():
    if environ.get('is_prod'):
        __secret = get_secret(secret_id=AWS_SECRET, region=AWS_REGION, is_json=True)
        FLASK_ENV = 'production'
        ENV = 'production'
        DEBUG = False
        TESTING = False
        SQLALCHEMY_DATABASE_URI = __secret.get('PROD_DATABASE_URI')
        SQLALCHEMY_TRACK_MODIFICATIONS = True
    else:
        log.warn("This is not prod")


class DevConfig():
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
