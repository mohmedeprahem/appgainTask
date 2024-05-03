from flask import Flask, request
from flask_pymongo import PyMongo
from flask_swagger_ui import get_swaggerui_blueprint


import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Your API Documentation"})

app.register_blueprint(swaggerui_blueprint)

from routes.item_routes import item_bp

app.register_blueprint(item_bp, url_prefix='/items')
