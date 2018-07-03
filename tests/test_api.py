# import unittest
import json
from api import app
from flask_testing import TestCase


class RideTestCase(TestCase):
    def setUp(self):
        self.sample_data = {
            'route': 'Kampala',
            'driver': '1',
            'fare': 5000
        }
    
    def create_app(self):
        initialize the test client
        return app

    def test_create_ride(self):
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res_data = json.loads(res.data.decode())
        print(res_data)
        # assert keys
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('_id', res_data)
        # assert expected data
        self.assertEqual(res_data['status'], 'OK')
        # assert expected status code
        self.assertEqual(res.status_code, 201)

    def test_create_ride_with_invalid_data(self):
        self.sample_data = {
            'route': 123,
            'driver': 156,
            'fare': "5000"
        }
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res_data = json.loads(res.data.decode())
        # assert keys
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        # assert expected data
        self.assertEqual(res_data['status'], 'fail')
        # assert expected status code
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 201)

    def test_get_all_rides(self):
        res = self.client.post('/api/v1/rides', 
                            data=json.dumps(self.sample_data),
                            content_type='application/json')
        res = self.client.get('/api/v1/rides',
                            data=json.dumps(self.sample_data),
                            content_type='application/json')
        res_data = json.loads(res.data.decode())
        # assert expected data
        self.assertEqual(res_data['status'], 'OK')
        # assert expected status code
        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_get_a_specific_ride(self):
        res = self.client.post('/api/v1/rides',
                            data=json.dumps(self.sample_data),
                            content_type='application/json')
        res = self.client.get('/api/v1/rides/1',
                            data=json.dumps(self.sample_data),
                            content_type='application/json')
        res_data = json.loads(res.data.decode())
        # assert expected data
        self.assertEqual(res_data['status'], 'OK')
        # assert expected status code
        self.assertEqual(res.status_code, 200)

    def test_join_a_ride(self):
        self.sample_data = {
            'passenger': '1',
            'ride': '1'
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
            'username':'Inno',
            'email': 'Inno@gmail.com',
            'password':'12345',
            'contact':'0702-811121'
        }
        res = self.client.post('/auth/signup',
                            data=json.dumps(self.sample_data),
                            content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'], 'OK')
        # assert expected status code
        self.assertEqual(res.status_code, 201)
        # assert keys
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('username', res_data)
        self.assertIn('id', res_data)

    def test_signup_with_invalid_data(self):
        self.sample_data = {
            'username':'tester',
            'email': 'tester.com',
            'password':'12345',
            'contact':'0702811121'
        }
        res = self.client.post(
            '/auth/signup',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res_data = json.loads(res.data.decode())
        # assert keys
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        # assert expected data
        self.assertEqual(res_data['status'], 'fail')
        # assert expected status code
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 201)

    def test_login(self):
        self.sample_data = {
            'username':'tester',
            'email': 'tester@mail.com',
            'password':'12345',
            'contact':'0702-811121'
        }
        signup_data = self.client.post('/auth/signup',
                            data=json.dumps(self.sample_data),
                            content_type='application/json')
        response_data = json.loads(signup_data.data.decode())
        self.sample_data = {
            'email': 'tester@mail.com',
            'password':'12345'
        }
        # pick client data and decode it
        res = self.client.post('/auth/login',
                            data=json.dumps(self.sample_data),
                            content_type='application/json')
        res_data = json.loads(res.data.decode())
        # assert expected status
        self.assertEqual(res_data['status'], 'OK')
        # assert expected status code
        self.assertEqual(res.status_code, 200)
        # assert keys
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('access_token', res_data)
    
    def test_get_requests_by_id(self):
        self.sample_data = {
            'passenger': '1',
            'ride': '1'
        }
        res = self.client.post('/api/v1/rides/1/requests',
                               data=json.dumps(self.sample_data),
                               content_type='application/json')
        res = self.client.get('/api/v1/users/rides/1/requests',
                              data=json.dumps(self.sample_data),
                              content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'], 'OK')
        # assert expected status code
        self.assertEqual(res.status_code, 200)
        # assert keys
        self.assertIn('status', res_data)
        self.assertIn('message', res_data)
        self.assertIn('ride_requests', res_data)
