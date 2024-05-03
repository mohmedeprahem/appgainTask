from flask import Flask
from flask_pymongo import PyMongo


import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

from routes.item_routes import item_bp

app.register_blueprint(item_bp, url_prefix='/items')

