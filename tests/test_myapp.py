import unittest
from app import app, mongo
from flask_pymongo import PyMongo
import json


class TestRegistration(unittest.TestCase):

  def setUp(self):
      app.config['TESTING'] = True
      self.app = app.test_client()


  def tearDown(self):
      with app.app_context():
        collections = mongo.db.list_collection_names()
        for collection_name in collections:
            mongo.db.drop_collection(collection_name)

  def test_registration(self):
    user_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password"
  }

    # Convert the user data to JSON format
    json_data = json.dumps(user_data)

    # Sending a POST request to register a new user with JSON data
    response = self.app.post('/auth/register',
      data=json_data,
      content_type='application/json',
      follow_redirects=True)

    self.assertEqual(response.status_code, 201)

    with app.app_context():
      user = mongo.db.users.find_one({'username': 'testuser'})
      self.assertIsNotNone(user)
      self.assertEqual(user['email'], 'test@example.com')

  def test_successful_login(self):
    login_data = {
      "email": "test@example.com",
      "password": "password"
    }
    response = self.app.post('/auth/login',
      data=json.dumps(login_data),
      content_type='application/json')

    data = json.loads(response.data.decode('utf-8'))

    self.assertEqual(response.status_code, 200)

    self.assertTrue(data['success'])
    self.assertIn('token', data)

if __name__ == '__main__':
    unittest.main()
