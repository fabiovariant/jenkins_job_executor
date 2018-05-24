import mysql.connector

self.MYSQL_USER = os.environ['MYSQL_USER']
self.MYSQL_PASS = os.environ['MYSQL_PASS']

def get_connection():
    return mysql.connector.connect(user=MYSQL_USER, database=MYSQL_PASS)