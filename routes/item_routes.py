from flask import Blueprint, request
from app import mongo

item_bp = Blueprint('item', __name__)

db = mongo.db.items

@item_bp.route('/', methods=['POST'])
def add_items():
    data = request.get_json()
    db.insert_one(data)
    return 'Item added successfully' , 201
