

total_rides = []

class Rides:
    def __init__(self,_id,route,driver,fare):
        '''rides class'''
            
        _id = len(total_requests)
        _id += 1
        self._id = _id
        self.route = route
        self.driver = driver
        self.fare = fare       
        self.total_rides = []

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

        new_ride = {
            '_id':self._id,
            'route':self.route,
            'driver': self.driver,
            'fare':self.fare
        }

        total_rides.append(new_ride)
        return new_ride






# class RideRequests:
#     def __init__(self,request_id=None,username=None,contact=None):
#         self.request_id = request_id
#         self.username = username
#         self.contact = contact
    
#     def get_request_id(self):
#         return self.request_id
    
#     def get_username(self):
#         return self.username
    
#     def get_contact(self):
#         return self.contact

# ride_requests = []