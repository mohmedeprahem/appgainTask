from flask import Blueprint, request
from app import mongo
from schemas.item_schemas import ItemSchema
from marshmallow import ValidationError

item_bp = Blueprint('item', __name__)

db = mongo.db.items

@item_bp.route('/', methods=['POST'])
def add_items():
    try:
        data = request.get_json()
        ItemSchema().load(data)
        db.insert_one(data)
        return 'Item added successfully' , 201
    except ValidationError as error:
        return error.messages, 400
