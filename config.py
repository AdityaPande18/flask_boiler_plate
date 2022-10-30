from app.utils.aws_utils import get_secret
from constants import AWS_SECRET, AWS_REGION
from os import environ

class FlaskConfig():
    def __init__(self, env=None):
        self.config_dict = {}
        if(env=='development'):
            self.config_dict = self.devConfig()
        elif(env=='production'):
            self.config_dict = self.prodConfig()
        else:
            raise Exception('Environment not specified! Possible values: development or production')

    def devConfig(self):
        config = {
            'FLASK_ENV': 'development',
            'ENV': 'development',
            'DEBUG': True,
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': environ.get('DEV_DATABASE_URI', 'sqlite:///database.db'),
            'SQLALCHEMY_TRACK_MODIFICATIONS': True,
        }
        return config

    def prodConfig(self):
        __secret = get_secret(secret_id=AWS_SECRET, region=AWS_REGION, is_json=True)
        config = {
            'FLASK_ENV': 'production',
            'ENV': 'production',
            'DEBUG': False,
            'TESTING': False,
            'SQLALCHEMY_DATABASE_URI': __secret.get('PROD_DATABASE_URI'),
            'SQLALCHEMY_TRACK_MODIFICATIONS': True,
        }
        return config