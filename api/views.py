from flask import Flask, jsonify, request
from .models import Rides, RideRequests, rides
from .validators import schema
from jsonschema import validate
from api import app

@app.route('/api/v1/rides' ,methods= ['POST'])
def create_ride():
    ride_data = request.get_json()
    try:
        validate({'route':ride_data['route'],'driver':ride_data['driver'], 'fare':ride_data['fare']},schema)        
        new_ride = Rides(ride_data['route'],ride_data['driver'],ride_data['fare'])
        new_ride.add_ride()
        try:           
            return jsonify({
                'status':'OK',
                'message': 'Ride successfully created',
                '_id':new_ride.get_id()
            }), 201
        except:
            return jsonify({ 
                'status':'FAIL',
                'message': 'Failed to create ride'
            }), 400                         
    except:
        return jsonify({
        'status': 'FAIL',
        'message': 'Failed to create Ride. Invalid ride data',
    }), 400


@app.route('/api/v1/rides',methods=['GET'])
def get_all_rides():
 
    if len(rides) < 1:
        return jsonify({
            'status':'FAIL',
            'message':"you have no rides"
        }),404
    return jsonify({
        'status':'OK',
        'requests':rides,
        'message':'Successfully returned all Rides'
}),200

@app.route('/api/v1/rides/<_id>',methods=['GET'])
def get_a_specific_ride(_id):
    
    results = Rides.get_a_specific_ride(_id)
    if results:
        return jsonify({        
            'results':results,
            'status':'OK',
            'response_message':'Successfully returned Ride',
        }),200
    else:
        return jsonify({        
            'response_message':'Ride does not exist',
            'status':'FAIL'
}),200 
 


@app.route('/api/v1/rides/<_id>/requests', methods=['POST'])
def join_a_ride(_id):
    ride = rides[int(_id) - 1]
    if ride:
        
        request_data = request.get_json()
        if isinstance(request_data['username'], str) and  isinstance(request_data['contact'], str):
        
            request_ride = RideRequests(request_data['username'],request_data['contact'])
            request_ride.join_ride()
            if request_ride:            
                return jsonify({
                    'status':'OK',
                    'message': 'Ride request successfully created',
                    'request_id':request_ride.get_request_id(),
                    'ride_id': ride.get("_id")
                }), 201
            else:
                return jsonify({ 
                    'status':'FAIL',
                    'response_message': 'Failed to create Ride request'
                }), 400
        return jsonify({
        'status': 'FAIL',
        'response_message': 'Failed to create Ride. Invalid request data',}), 400
    return jsonify({
        'status': 'FAIL',
        'response_message': 'Ride ID not found',
    }),400


