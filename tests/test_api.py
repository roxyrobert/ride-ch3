# import unittest
import json
from api import app
from flask_testing import TestCase
from api.db import DBConnection

connect = DBConnection()
cursor = connect.cursor


class RideTestCase(TestCase):

    def setUp(self):
        global cursor
        connect.delete_tables()
        connect.create_tables()

        self.sample_data = {
            'route': 'Kampala',
            'driver': '1',
            'fare': 5000
        }

    def create_app(self):
        # initialize the test client
        return app

    def test_create_ride(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')

        self.sample_data = {
            'route': 'Kampala',
            'driver': 1,
            'fare': 5000
        }
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res_data = json.loads(res.data.decode())
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('_id', res_data)
        self.assertEqual(res_data['status'], 'OK')
        self.assertEqual(res.status_code, 201)

    def test_create_ride_with_invalid_data(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'route': 123,
            'driver': 0,
            'fare': "5000"
        }
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res_data = json.loads(res.data.decode())
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertEqual(res_data['status'], 'fail')
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 201)

    def test_get_all_rides(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'email': 'tester@mail.com',
            'password': '12345678'
        }
        res = self.client.post('/api/v1/auth/login',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res_data = json.loads(res.data.decode())
        token = res_data["access_token"]
        
        self.sample_data = {
            'route': 'Kampala',
            'driver': 1,
            'fare': 5000
        }
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json',
            headers=dict(Authorization= Bearer + token)
        )

        res = self.client.post('/api/v1/rides', 
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res = self.client.get('/api/v1/rides',
                              data=json.dumps(self.sample_data),
                              content_type='application/json')
        res_data = json.loads(res.data.decode())

        self.assertEqual(res_data['status'], 'OK')

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_get_specific_ride(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'route': 'Kampala',
            'driver': 1,
            'fare': 5000
        }
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res = self.client.post('/api/v1/rides',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res = self.client.get('/api/v1/rides/1',
                              data=json.dumps(self.sample_data),
                              content_type='application/json')
        res_data = json.loads(res.data.decode())

        self.assertEqual(res_data['status'], 'OK')

        self.assertEqual(res.status_code, 200)

    def test_join_a_ride(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'route': 'Kampala',
            'driver': 1,
            'fare': 5000
        }
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        self.sample_data = {
            'passenger': 1,
            'ride': 1
        }
        res = self.client.post('/api/v1/rides/1/requests',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'], 'OK')
        # assert expected status code
        self.assertEqual(res.status_code, 201)
        # assert keys
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('request_id', res_data)
        self.assertIn('ride_id', res_data)

    def test_signup(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@gmail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        res = self.client.post('/api/v1/auth/signup',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'], 'OK')

        self.assertEqual(res.status_code, 201)
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('username', res_data)
        self.assertIn('id', res_data)

    def test_signup_with_invalid_data(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester.com',
            'password': '12345',
            'contact': '0702811121'
        }
        res = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res_data = json.loads(res.data.decode())
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertEqual(res_data['status'], 'fail')
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 201)

    # Test login with valid data inputs
    def test_login(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'email': 'tester@mail.com',
            'password': '12345678'
        }
        res = self.client.post('/api/v1/auth/login',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'], 'OK')
        self.assertEqual(res.status_code, 200)
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('access_token', res_data)

    def test_login_with_invalid_data(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'email': 'te.com',
            'password': '12'
        }
        res = self.client.post('/api/v1/auth/login',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'], 'fail')
        self.assertEqual(res.status_code, 400)
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)

    def test_get_requests_by_id(self):
        self.sample_data = {
            'username': 'tester',
            'email': 'tester@mail.com',
            'password': '12345678',
            'contact': '0702-811121'
        }
        self.client.post('/api/v1/auth/signup',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'route': 'kampala',
            'driver': 1,
            'fare': 7000
        }
        self.client.post('/api/v1/rides',
                         data=json.dumps(self.sample_data),
                         content_type='application/json')
        self.sample_data = {
            'passenger': 1,
            'ride': 1
        }
        res = self.client.post('/api/v1/rides/1/requests',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res = self.client.get('/api/v1/users/rides/1/requests',
                              data=json.dumps(self.sample_data),
                              content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'], 'OK')
        self.assertEqual(res.status_code, 200)
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('ride_requests', res_data)
