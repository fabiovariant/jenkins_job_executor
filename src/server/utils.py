import mysql.connector
import os

MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']

config = {
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASS'],
    'host': os.environ['MYSQL_HOST'],
    'port': os.environ['MYSQL_PORT'],
    'database': 'jenkins_executor'
}

def get_connection():
    return mysql.connector.connect(**config)

if __name__ == '__main__':
    cnx = get_connection()
    sql = 'SELECT cd_user_Type, ds_user_type FROM Dm_User_type'
    cur = cnx.cursor(buffered=True)
    cur.execute(sql)
    for (cd_user_Type, ds_user_type) in cur:
        print('User ' + cd_user_Type)