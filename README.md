# ride [![Build Status](https://travis-ci.org/roxyrobert/ride.svg?branch=endpoints)](https://travis-ci.org/roxyrobert/ride)
# ride [![Coverage Status](https://coveralls.io/repos/github/roxyrobert/ride/badge.svg?branch=master)](https://coveralls.io/github/roxyrobert/ride?branch=endpoints2)

# Ride-my-Way API  [![Build Status](https://travis-ci.org/roxyrobert/ride.svg?branch=master)](https://travis-ci.org/roxyrobert/ride)

Ride-my App is a carpooling application that provides drivers with the ability to create ride offers 
and passengers to join available ride offers.

## Tools
Tools used during the development of this API are;
- [JWT](https://jwt.io) - JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.
- JWT.IO allows you to decode, verify and generate JWT.
- [Flask](http://flask.pocoo.org/) - this is a python micro-framework
- [Postgresql](https://www.postgresql.org/) - this is a database server


## Requirements
- Python 3.6.5
- Flask framework
## Testing frame
- nosetests nose==1.3.7
- Execute the following command in your terminal to run the tests- $ nosetests --with-coverage

## Running the application
- Use Postman to test the endpoints
 
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


