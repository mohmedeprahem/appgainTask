from flask import Blueprint, request, jsonify, render_template
from app import mongo
from datetime import datetime
from bson import ObjectId
from decorators.auth_decorator import token_required
from utils.email_utils import send_email

order_bp = Blueprint('order', __name__)

db = mongo.db

@order_bp.route('/add', methods=['POST'])
@token_required
def add_order(current_user):

  # start transaction
  with mongo.cx.start_session() as session:
    with session.start_transaction():
      try:
        total_price = 0

        order = {
          'customer_id': current_user['_id'],
          'order_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
          'items': [],
          'total_price': total_price
        }

        data = request.get_json()
        if data is None:
          return 'Item is required', 400

        for item in data:
          if item.get('id') is None or item.get('count') is None:
            return 'Item id and count are required', 400

        for item in data:
          item_id = ObjectId(item['id'])
          itemInfoDB = db.items.find_one({'_id': item_id})

          if itemInfoDB is None:
            session.abort_transaction()
            return 'Item {} not found'.format(item['id']), 404
          else:
            if 0 >= item['count']:
              session.abort_transaction()
              return 'Item count must be greater than 0', 400

            if itemInfoDB['count'] < item['count']:
              session.abort_transaction()
              return 'Item {} is out of stock'.format(itemInfoDB['name']), 400

            total_price += itemInfoDB['price'] * item['count']

            db.items.update_one({'_id': item_id}, {'$set': {'count': itemInfoDB['count'] - item['count']}}, session=session)

            order['items'].append({
              'name': itemInfoDB['name'],
              'price': itemInfoDB['price'],
              'count': item['count']
            })

        order['total_price'] = total_price
        db.orders.insert_one(order, session=session)

        session.commit_transaction()
      except Exception as e:
        session.abort_transaction()
        return 'Internal server error', 500

      try:
        order['_id'] = str(order['_id'])
        html_content = render_template('order_confirmation_email.html', order=order)
        is_sent = send_email('Order Confirmed', [current_user['email']], html_content)

        if not is_sent:
          return 'order Confirmed successfully but email not sent', 201

        return 'Order added successfully, Check your email', 201
      except Exception as e:
        return 'Internal server error', 500
