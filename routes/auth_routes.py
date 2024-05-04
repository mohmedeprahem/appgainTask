from flask import Blueprint, request, jsonify
import jwt, bcrypt
from app import mongo, app
from schemas.register_schemas import RegisterSchema
from marshmallow import ValidationError
from datetime import datetime, timedelta



auth_bp = Blueprint('auth', __name__)

db = mongo.db.users

@auth_bp.route('/register', methods=['POST'])
def register():
  try:
    data = request.get_json()
    RegisterSchema().load(data)
    UserExists = db.find_one({'email': data['email']})
    if UserExists:
      return jsonify({
            'success': False,
            'statusCode': 209,
            'message': 'User already exists'
        }), 409
    data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    db.insert_one(data)
    return jsonify({
            'success': True,
            'statusCode': 201,
            'message': 'User already exists'
        }), 201
  except ValidationError as error:
    return jsonify({
            'success': False,
            'statusCode': 400,
            'message': error.messages,
        }), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = db.find_one({'email': data['email']})
    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
      # Generate JWT token
      token = jwt.encode({
          'user_id': str(user['_id']),
          'exp': datetime.utcnow() + timedelta(hours=1)
      }, app.config['JWT_SECRET_KEY'], algorithm='HS256')

      return jsonify({
          'success': True,
          'statusCode': 200,
          'message': 'User logged in successfully',
          'token': token
      }), 200
    else:
      return jsonify({
          'success': False,
          'statusCode': 401,
          'message': 'Invalid email or password'
      }), 401
