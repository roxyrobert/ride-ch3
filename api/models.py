from flask import Flask, jsonify, request
from api import cur, conn


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
        '''create a new_ride'''

        cur.execute(
            "INSERT INTO rides (route, driver, fare) VALUES ('{}','{}','{}')"
            .format(self.route, self.driver, self.fare))
        conn.commit()

        cur.execute(
            "SELECT id FROM rides WHERE driver = '{}' ORDER BY created_at DESC"
            .format(self.driver))
        record = cur.fetchone()
        self.id = record[0]
        new_ride = {
            'id': self.id,
            'route': self.route,
            'driver': self.driver,
            'fare': self.fare
        }

        return new_ride

    @staticmethod
    def get_a_specific_ride(id):
        """fetch a ride by id"""
        cur.execute(
            "SELECT * FROM rides WHERE id = '{}'".format(id))
        record = cur.fetchone()
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
        cur.execute(
            "SELECT * FROM rides")
        record = cur.fetchall()
        if len(record) > 0:
            return record


class RideRequests:
    def __init__(self, passenger, ride):
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
        cur.execute(
            "INSERT INTO requests (passenger, ride) VALUES ('{}','{}');"
            .format(self.passenger, self.ride))
        conn.commit()
        print("here")

        cur.execute(
            "SELECT * FROM requests WHERE passenger = '{}' ORDER BY created_at DESC;".format(self.passenger))
        record = cur.fetchone()

        self.id = record[0]
        if len(record) > 0:
            self.id = record[0]
            ride_request = {
                    '_id': self.id,
                    'passenger': record[1],
                    'ride': record[2]
                }
            return ride_request
