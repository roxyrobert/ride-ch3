from flask import Flask, jsonify, request
from .models import Rides, RideRequests, Users
from .validators import create_ride_schema, join_ride_schema, users_schema, login_schema
from jsonschema import validate
from api import cur, conn
from api import app


@app.route('/auth/signup', methods=['POST'])
# This endpoints creates a new user in the database
def signup():
    '''This endpoint create a new user account'''
    user_data = request.get_json()
    cur.execute(
            "SELECT email FROM users WHERE email='{}'".format(user_data['email']))
    record = cur.fetchone()
    if record is None:
        try:

            validate({'username': user_data['username'],
                     'email': user_data['email'],
                      'password': user_data['password'],
                      'contact': user_data['contact']}, users_schema)

            new_user = Users(user_data['username'], user_data['email'],
                            user_data['password'], user_data['contact'])

            new_user.create_user()

            return jsonify({
                    'status': 'OK',
                    'message': 'New user successfully created',
                    'username': new_user.get_username(),
                    'id': new_user.get_id()
                }), 201
        except:
            return jsonify({
                'status': 'fail',
                'message': 'failed to create user. Invalid user data entered',
                }), 400
    else:
        return jsonify({
                'status': 'fail',
                'message': 'user already exists'
        })

@app.route('/auth/login', methods=['POST'])
def signin():
    '''This endpoint enables a user to login'''
    login_data = request.get_json()
    try:
        validate({'email': login_data['email'],
            'password': login_data['password']}, login_schema)
    except:
        return jsonify({
            'status':'fail',
            'message':'invalid login data'
        }), 400
            
    # Get user by email
    cur.execute(
        "SELECT * FROM users WHERE email='{}'".format(login_data['email']))
    user = cur.fetchone()

    if len(user) > 0:

        user_object = Users(user[1], user[2], user[3], user[4])
        
        user_token = user_object.get_token()
        return jsonify({
            'status': 'OK',
            'message': 'logged in succesfully',
            'access_token': user_token.decode('utf8')
            }), 200
    


@app.route('/api/v1/rides', methods=['POST'])
def create_ride():
    """This endpoint creates a new ride and commits it to the database"""
    ride_data = request.get_json()
    try:
        validate({'route': ride_data['route'],
                 'driver': ride_data['driver'],
                  'fare': ride_data['fare']}, create_ride_schema)

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
            'status': 'fail',
            'message': 'failed to create Ride. Invalid ride data',
            }), 400


@app.route('/api/v1/rides', methods=['GET'])
# This endpoint gets all rides
def get_all_rides():
    results = Rides.get_all_rides()
    if len(results) > 0:
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
    else:
        return jsonify({
            'status': 'not found',
            'message': 'There are no ride offers'
        }), 404



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
            'status': 'fail'
        }), 404


@app.route('/api/v1/rides/<_id>/requests', methods=['POST'])
def join_a_ride(_id):
    # This endpoint enables a user to make a request to join a ride offer

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

@app.route('/api/v1/users/rides/<ride_Id>/requests', methods=['GET'])
def get_requests_by_id(ride_Id):
    ''' This endpoint returns all requests to a specific ride_offer'''
    results = RideRequests.get_requests_for_ride(ride_Id)
    if len(results) > 0:
        requests_list = []
        for result in results:
            ride_request = {
                'id': result[0],
                'passenger': result[1],
                'ride': result[2]
            }
            requests_list.append(ride_request)
        return jsonify({
            'status': 'OK',
            'message': 'Ride requests returned',
            'ride_requests': requests_list
        }), 200
    else:
        return jsonify({
            'status': 'not found',
            'message': 'There are no requests to the offer'
        }), 404

@app.route('/users/rides/<ride_id>/requests/<request_id>', methods=['PUT'])
def accept_or_reject(ride_id, request_id):
    # This endpoint enables a user to accept or reject a ride_request
    status = request.get_json().get('status', False)
    if status:
        message = 'Ride request Accepted'
    else:
        message = 'Ride request Rejected'
    cur.execute(
        "UPDATE requests SET status={} WHERE id ='{}'".format(status, request_id))
    conn.commit()
    return jsonify({
        'message': message,
        'status':'ok'
    })
