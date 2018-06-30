import psycopg2
from flask import Flask

app = Flask(__name__)

# Connect to an existing database
conn = psycopg2.connect("dbname=ride user=roxy")

# Open a cursor to perform database operations
cur = conn.cursor()

from api import views
