from flask import Flask
from flask_restx import Api
from app.controller.home import home_ns
from app import db
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return "Hello World!"

# app.add_url_rule('/home', view_func=index)

class FlaskAppWrapper():
    def __init__(self, **configs):
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
        self.app.config.from_object('config.DevConfig')


    def initialize_namespaces(self):
        self.api.add_namespace(ns=home_ns)


    def run(self, **kwargs):
        self.app.run(**kwargs)

if __name__ == "__main__":
    FlaskAppWrapper()