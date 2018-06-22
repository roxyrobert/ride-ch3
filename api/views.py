from flask import Flask, jsonify, request
from .models import Rides, total_rides
from api import app


@app.route('/api/v1/rides' ,methods= ['POST'])
def create_ride():
   
    ride_data = request.get_json()
    
    if isinstance(ride_data['route'], str) and  isinstance(ride_data['driver'], str) and isinstance(ride_data['fare'], int):
        
        new_ride = Rides(ride_data['route'],ride_data['driver'],ride_data['fare'])
        new_ride.add_ride()
        if new_ride:            
            return jsonify({
                'status':'OK',
                'response_message': 'Ride successfully created',
                '_id':new_ride.get_id()
            }), 201
        else:
            return jsonify({ 
                'status':'FAIL',
                'response_message': 'Failed to create ride'
            }), 400            
                   
    return jsonify({
        'status': 'FAIL',
        'response_message': 'Failed to create Ride. Invalid ride data',
}), 400


@app.route('/api/v1/rides',methods=['GET'])
def get_all_rides():
 
    if len(total_rides) < 1:
        return jsonify({
            'status':'FAIL',
            'response_message':"you have no rides"
        }),404
    return jsonify({
        'status':'OK',
        'requests':total_rides,
        'message':'Successfully returned request'
}),200
 

    

# @app.route('/api/v1/rides/<_id>', methods=['GET'])
# def get_a_specific_ride(_id):
#     ride = request.get_json(_id)
#     if not ride:
#         return jsonify({'message':'No ride found'})
#     for ride in rides:
#         if ride[_id] == _id:
#             return jsonify({"ride":ride})
#         else:
#             return jsonify({"message":"id not found"})


# @app.route('/api/v1/join_ride', methods=['POST'])
# def join_a_ride():
#     data = request.get_json()
#     if len(ride_requests) > 0:
#         request_id +=1
#     new_request = RideRequests(username =data["username"], contact =data["contact"])
#     ride_requests.append(new_request)
#     return jsonify({'message':'new ride request added'})

