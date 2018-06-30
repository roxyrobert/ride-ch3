from flask import Flask, jsonify, request
from .models import Rides, RideRequests
from .validators import schema, join_ride_schema
from jsonschema import validate
from api import app


@app.route('/api/v1/rides', methods=['POST'])
# This endpoint creates a new ride and appends it to the rides list
def create_ride():
    ride_data = request.get_json()
    try:
        validate({'route': ride_data['route'],
                 'driver': ride_data['driver'],
                  'fare': ride_data['fare']}, schema)

        new_ride = Rides(ride_data['route'], ride_data['driver'],
                         ride_data['fare'])
        new_ride.add_ride()
        return jsonify({
                'status': 'OK',
                'message': 'Ride successfully created',
                '_id': new_ride.get_id()
            }), 201

    except:
        return jsonify({
            'status': 'FAIL',
            'message': 'Failed to create Ride. Invalid ride data',
            }), 400


@app.route('/api/v1/rides', methods=['GET'])
# This endpoint gets all rides
def get_all_rides():
    results = Rides.get_all_rides()
    rides_list = []
    for result in results:
        ride = {
            'id': result[0],
            'route': result[1],
            'driver': result[2],
            'fare': result[3],
            'created_at': result[4]
        }
        rides_list.append(ride)
    return jsonify({
        'status': 'OK',
        'rides': rides_list
    }), 200


@app.route('/api/v1/rides/<_id>', methods=['GET'])
# This endpoint gets a specific ride by id
def get_a_specific_ride(_id):

    results = Rides.get_a_specific_ride(_id)  # to get a ride by id

    try:
        return jsonify({
            'results': results,
            'status': 'OK',
            'response_message': 'Successfully returned Ride',
        }), 200
    except:
        return jsonify({
            'response_message': 'Ride does not exist',
            'status': 'FAIL'
        }), 404


@app.route('/api/v1/rides/<_id>/requests', methods=['POST'])
def join_a_ride(_id):

    request_data = request.get_json()
    request_ride = RideRequests(request_data['passenger'],
                                    request_data['ride'])
    request_ride.join_ride()
    return jsonify({
        'status': 'OK',
        'message': 'Ride request successfully created',
        'request_id': request_ride.get_request_id(),
        'ride_id': _id
    }), 201
