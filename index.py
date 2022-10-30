from flask import Flask
from flask_restx import Api
from app.controller.home import home_ns
from app import db

from config import FlaskConfig

class FlaskAppWrapper():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, title='Boiler Plate', description='A Flask boiler plate to start new project')
        self.configs()
        self.setup_database()
        self.initialize_namespaces()

        # After startup operations run the app
        self.run()

    def setup_database(self):
        db.init_app(self.app)

    def configs(self):
        config_obj = FlaskConfig(env='development')
        for key, val in config_obj.config_dict.items():
            self.app.config[key] = val


    def initialize_namespaces(self):
        self.api.add_namespace(ns=home_ns)


    def run(self, **kwargs):
        self.app.run(**kwargs)

if __name__ == "__main__":
    FlaskAppWrapper()