from flask import Flask, Blueprint
from app.config.config import config
from app.myapp.api import myapi
from app.view.home import home

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.route('/')
    def index():
        return 'This is index, ' + app.config['TYPE']

    app.register_blueprint(myapi)
    app.register_blueprint(home)
    return app