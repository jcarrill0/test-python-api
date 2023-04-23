from flask import Flask
from api.routes import api

def create_app():
    app = Flask(__name__)
    # Add all endpoints form the API with a "api" prefix
    app.register_blueprint(api, url_prefix='/api')
    return app