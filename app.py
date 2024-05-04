from flask import Flask, request
from flask_pymongo import PyMongo
from flask_swagger_ui import get_swaggerui_blueprint
from flask_mail import Mail, Message

import os

app = Flask(__name__)

# init database
if os.environ.get("ENV") == "test":
    app.config["MONGO_URI"] = os.environ.get("TESTING_MONGO_URI")
else:
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
print(app.config["MONGO_URI"])

mongo = PyMongo(app)

# init jwt
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY') or 'you-will-never-guess'

# init swagger
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Your API Documentation"})

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jobjobjobpro@gmail.com'
app.config['MAIL_PASSWORD'] = 'shfj etrz opcq pztc'
app.config['MAIL_DEFAULT_SENDER'] = 'jobjobjobpro@gmail.com'
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

app.register_blueprint(swaggerui_blueprint)

from routes.item_routes import item_bp
from routes.auth_routes import auth_bp
from routes.order_routes import order_bp

app.register_blueprint(item_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(order_bp, url_prefix='/orders')
