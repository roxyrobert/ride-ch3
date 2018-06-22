

total_rides = []

class Rides:
    def __init__(self,route,driver,fare):
        '''rides class'''
            
        _id = len(total_rides)
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

    @staticmethod
    def get_a_specific_ride(_id):
        
        _id = int(_id) 
        if len(total_rides) > 0 and _id <= len(total_rides):
            ride_data = {
                '_id': total_rides[_id-1]['_id'],
                'route': total_rides[_id-1]['route'],
                'driver': total_rides[_id-1]['driver'],
                'fare': total_rides[_id-1]['fare'],
            }
            return ride_data




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