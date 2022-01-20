import mysql.connector

from flask import jsonify
from getpass import getpass
from mysql.connector import connect, Error
from mysql.connector import connection
from mysql.connector import DatabaseError

class Location:
    def __init__(self, id):
        self.id = id

    def get_saved_locations(self):
        get_user_locations_query = "SELECT id, name, street_address, city, state "\
                                    "from commemoro.location WHERE user_id {0}".format(self.id)
        user_locations = []
        try:
            with connect (
                host="commemoro-dev.cqvntilgmgqn.us-east-1.rds.amazonaws.com",
                user="commemoro-api",
                password = "CodeForce2010!!"
            ) as connection:
                with connection.cursor () as cursor:
                        cursor.execute(get_user_locations_query)
                        result = cursor.fetchall()
                        for row in result:
                            print(row)
                            location = {
                                "user_id": self.id,
                                "name": row[0],
                                "street_address": row [1],
                                "city": row [2],
                                "state": row [3]
                            }
                            user_locations.append(location)

                try:
                    return jsonify(user_locations)
                except:
                    return jsonify({"Message": "No Locations Found"}), 204
        except Error as e:
                print (e)
