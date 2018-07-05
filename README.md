# Ride-my-Way API  [![Build Status](https://travis-ci.org/roxyrobert/ride.svg?branch=master)](https://travis-ci.org/roxyrobert/ride)

Ride-my App is a carpooling application that provides drivers with the ability to create ride offers 
and passengers to join available ride offers.
 
## Endpoints 
HTTP Method|End point |Action
-----------|----------|--------------
POST | /api/v1/auth/signup | Register a user
POST | /api/v1/auth/login | Login a user
GET| /api/v1/rides   | Fetch all ride offers
GET | /api/v1/rides/<_id> | Fetch a single ride offer
POST | /api/v1/rides | Create a ride offer
GET| /api/v1/users/<ride_id>/requests   | Fetch all ride offers
POST | /api/v1/rides/<_id>/requests  | Make a request to join a ride
PUT | /api/v1/users/rides/<ride_id>/request/request_id | Create a ride offer


## Requirements
- Python 3.6.5
- Flask framework
## Testing frame
- nosetests

## Running the application
- Use Postman to test the endpoints
