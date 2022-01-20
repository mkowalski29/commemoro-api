import mysql.connector

from flask import jsonify
from getpass import getpass
from mysql.connector import connect, Error
from mysql.connector import connection
from mysql.connector.errors import DatabaseError


class User:
    def _init_(self, id):
        self.id = id

    def get_user_profile(self):
        get_user_profile_query = "SELECT email from commemoro.users WHERE user_id = {0}".format(self.id)
        try:
            with connect(
              host="commemoro-dev.cqvntilgmgqn.us-east-1.rds.amazonaws.com",
              user="commemoro-api",
              password="CodeForce2010!!"
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(get_user_profile_query)
                    result = cursor.fetchall()
            try:
                user_profile = {
                    "user_id": self.id,
                    "user_email": result[0][0]
                }   
                return jsonify(user_profile)
            except:
                user_profile = None
                return jsonify({"Error": "User Not Found"}), 401
        except Error as e:
            print (e)
