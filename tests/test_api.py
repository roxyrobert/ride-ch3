import unittest
import json
from api.views import app

class RideTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            'route':'A to B',
            'driver':'Robert',
            'fare': 5000
        }

        # initialize the test client
        self.client = app.test_client()

    def test_create_ride(self):
        res = self.client.post('/api/v1/rides', data=json.dumps(self.sample_data), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'],'OK')
    
    def test_get_all_rides(self):
        res = self.client.post('/api/v1/rides', data=json.dumps(self.sample_data), content_type='application/json')
        res = self.client.get('/api/v1/rides', data=json.dumps(self.sample_data), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'],'OK')

    def test_get_a_specific_ride(self):
        res = self.client.post('/api/v1/rides', data=json.dumps(self.sample_data), content_type='application/json')
        res = self.client.get('/api/v1/rides/1', data=json.dumps(self.sample_data), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertEqual(res_data['status'],'OK')



