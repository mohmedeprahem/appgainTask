from flask import Blueprint, request, jsonify
from app import mongo, bcrypt
from schemas.register_schemas import RegisterSchema
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt


auth_bp = Blueprint('auth', __name__)

db = mongo.db.users

@auth_bp.route('/register', methods=['POST'])
def register():
  try:
    data = request.get_json()
    RegisterSchema().load(data)
    UserExists = db.find_one({'email': data['email']})
    if UserExists:
      return 'User already exists', 409
    data['password'] = bcrypt.generate_password_hash('password').decode('utf-8')
    db.insert_one(data)
    return 'User added successfully' , 201
  except ValidationError as error:
    return error.messages, 400