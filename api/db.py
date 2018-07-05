
import psycopg2
import psycopg2.extras as extra
from pprint import pprint
from api import app


class DBConnection:
    def __init__(self):

   

    self.connection = psycopg2.connect(dbname="ride", user="roxy", password="1234", host="localhost")
    self.connection.autocommit = True
    self.cursor = self.connection.cursor()


    def create_tables(self):

        queries = (
            """
            CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            contact VARCHAR(100) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS rides(
            id SERIAL PRIMARY KEY,
            route VARCHAR(100) NOT NULL,
            driver INT references users(id),
            fare VARCHAR(100) NOT NULL,
            created_at TIMESTAMP default CURRENT_TIMESTAMP
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS requests(
            id SERIAL PRIMARY KEY,
            passenger INT references users(id),
            ride INT references rides(id),
            status BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMP default CURRENT_TIMESTAMP
            )
            """
        )
        for query in queries:
            self.cursor.execute(query)
    
    def delete_tables(self):
        queries = (
            """
            DELETE TABLE IF EXISTS user CASCADE
            """,

            """
            DELETE TABLE IF EXISTS rides CASCADE
            """,

            """
            DELETE TABLE IF EXISTS requests CASCADE
            """
        )
        for query in queries:
            self.cursor.execute(query)



if __name__ == "__main__":
    db = DBConnection()
    db.create_tables()
