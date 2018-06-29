import unittest
import json
from api.views import app


class RideTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            'route': 'A to B',
            'driver': 'Robert',
            'fare': 5000
        }

        # initialize the test client
        self.client = app.test_client()

    def test_create_ride(self):
        res = self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        res_data = json.loads(res.data.decode())
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
        self.assertEqual(res_data['status'], 'FAIL')
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
        self.assertEqual(res.status_code, 201)
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
        self.assertEqual(res.status_code, 201)

    def test_join_a_ride(self):
        self.sample_data = {
            'username': 'robert',
            'contact': '0702-811121'
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
