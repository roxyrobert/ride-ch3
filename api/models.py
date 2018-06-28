

rides = []

class Rides:
    def __init__(self,route,driver,fare):
        '''rides class'''
        self._id = 0
        self.route = route
        self.driver = driver
        self.fare = fare       
        self.rides = []

    def get_id(self):
        return self._id
    
    def get_route(self):
        return self.route

    def get_driver(self):
        return self.driver
    
    def get_fare(self):
        return self.fare
    
    def add_ride(self):
        '''create a new_ride'''

        _id = len(rides)
        self._id = _id + 1

        new_ride = {
            '_id':self._id,
            'route':self.route,
            'driver': self.driver,
            'fare':self.fare
        }

        rides.append(new_ride)
        return new_ride

    @staticmethod
    def get_a_specific_ride(_id):
        
        _id = int(_id) 
        if len(rides) > 0 and _id <= len(rides):
            ride_data = {
                '_id': rides[_id-1]['_id'],
                'route': rides[_id-1]['route'],
                'driver': rides[_id-1]['driver'],
                'fare': rides[_id-1]['fare'],
            }
            return ride_data


ride_requests = []

class RideRequests:
    def __init__(self,username,contact):
        self.request_id = 0
        self.username = username
        self.contact = contact
        self.ride_requests = []
    
    def get_request_id(self):
        return self.request_id
    
    def get_username(self):
        return self.username
    
    def get_contact(self):
        return self.contact
    
    def join_ride(self):
        '''request to join a ride'''

        request_id = len(ride_requests)
        self.request_id = request_id + 1

        request_ride = {
            'request_id':self.request_id,
            'username':self.username,
            'contact': self.contact
        }

        ride_requests.append(request_ride)
        return request_ride
