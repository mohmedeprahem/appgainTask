from flask import Blueprint, request, jsonify
from app import mongo
from schemas.item_schemas import ItemSchema
from marshmallow import ValidationError

item_bp = Blueprint('item', __name__)

db = mongo.db.items

@item_bp.route('/items', methods=['POST'])
def add_items():
    try:
        data = request.get_json()
        ItemSchema().load(data)
        db.insert_one(data)
        return 'Item added successfully' , 201
    except ValidationError as error:
        return error.messages, 400

@item_bp.route('/items', methods=['GET'])
def get_items():
    items = [item for item in db.find()]

    # Convert ObjectId to string for JSON serialization
    if items is not None:
        for item in items:
            item['_id'] = str(item['_id'])

        return jsonify({
            'success': True,
            'statusCode': 200,
            'items': items
        }), 200
    else:
        return jsonify({
            'success': False,
            'statusCode': 404,
            'message': 'No items found'
        }), 404
