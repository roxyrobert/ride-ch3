import jwt
from flask import jsonify
# from api import connection
from .db import DBConnection

db_connect = DBConnection()
connect = db_connect.connection
cursor = db_connect.connection.cursor()


class Users:

    def __init__(self, username, email, password, contact):
        '''users class'''
        self.id = 0
        self.username = username
        self.email = email
        self.password = password
        self.contact = contact

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_contact(self):
        return self.contact

    def create_user(self):
        '''create new user'''
        global cursor
        cursor.execute(
            """INSERT INTO users (username, email, password, contact) VALUES ('{}','{}','{}','{}')"""
            .format(self.username, self.email, self.password, self.contact))
        connect.commit()

        cursor.execute(
            """SELECT id FROM users WHERE username = '{}' ORDER BY id ASC"""
            .format(self.username))
        record = cursor.fetchone()
        self.id = record[0]
        new_user = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'contact': self.contact
        }

        return new_user

    def get_token(self):
        token = jwt.encode({'email': self.email}, 'secret', algorithm='HS256')
        return token

    def decode_token(self, token):
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
        if user['email'] == self.email:
            return True
        return False

    @staticmethod
    def get_all_users():
        """fetch all users"""
        global cursor
        cursor.execute(
            "SELECT * FROM users")
        records = cursor.fetchall()
        if len(records) > 0:
            users_list = []
            for record in records:
                user = {
                    'id': record[0],
                    'username': record[1],
                    'email': record[2],
                    'password': record[3],
                    'contact': record[4]
                }
                users_list.append(user)
            return users_list


class Rides:

    def __init__(self, route, driver, fare):

        '''rides class'''
        self.id = 0
        self.route = route
        self.driver = driver
        self.fare = fare

    def get_id(self):
        return self.id

    def get_route(self):
        return self.route

    def get_driver(self):
        return self.driver

    def get_fare(self):
        return self.fare

    def add_ride(self):
        '''create a new_ride offer'''
        global cursor
        cursor.execute(
            """INSERT INTO rides (route, driver, fare) VALUES ('{}','{}','{}')"""
            .format(self.route, self.driver, self.fare))
        connect.commit()

        cursor.execute(
            """SELECT id FROM rides WHERE driver = '{}' ORDER BY created_at DESC"""
            .format(self.driver))
        record = cursor.fetchone()
        self.id = record[0]
        new_ride = {
            'id': self.id,
            'route': self.route,
            'driver': self.driver,
            'fare': self.fare
        }

        return new_ride

    @staticmethod
    def get_specific_ride(_id):
        """fetch a ride by id"""
        global cursor
        cursor.execute(
            """SELECT * FROM rides WHERE id = '{}'""".format(_id))
        record = cursor.fetchone()
        if len(record) > 0:
            ride_data = {
                    '_id': record[0],
                    'route': record[1],
                    'driver': record[2],
                    'fare': record[3],
                }
            return ride_data
        else:
            return jsonify({
                'status': 'FAIL',
                'response_message': 'Ride ID not found',
            }), 404

    @staticmethod
    def get_all_rides():
        """fetch all rides"""
        global cursor
        cursor.execute(
            """SELECT * FROM rides""")
        record = cursor.fetchall()
        if len(record) > 0:
            return record


class RideRequests:
    def __init__(self, passenger=None, ride=None):
        self.id = 0
        self.passenger = passenger
        self.ride = ride

    def get_request_id(self):
        return self.id

    def get_passenger(self):
        return self.passenger

    def get_contact(self):
        return self.ride

    def join_ride(self):
        '''request to join a ride'''
        global cursor
        cursor.execute(
            """INSERT INTO requests (passenger, ride) VALUES ('{}','{}');"""
            .format(self.passenger, self.ride))
        connect.commit()

        cursor.execute(
            """SELECT * FROM requests WHERE passenger = '{}' ORDER BY created_at DESC;""".format(self.passenger))
        record = cursor.fetchone()

        self.id = record[0]
        if len(record) > 0:
            self.id = record[0]
            ride_request = {
                    '_id': self.id,
                    'passenger': record[1],
                    'ride': record[2]
                }
            return ride_request
    
    @staticmethod
    def get_requests_for_ride(id):
        '''get all ride requests to a specific ride offer'''
        global cursor
        cursor.execute(
            """SELECT * FROM requests WHERE ride = '{}'""".format(id))
        ride_requests = cursor.fetchall()
        if len(ride_requests) > 0:
            return ride_requests
