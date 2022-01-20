import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error
from mysql.connector.errors import DatabaseError



try:
    with connect(
        host = "commemoro-dev.cqvntilgmgqn.us-east-1.rds.amazonaws.com", 
        user=input("Enter username: "),
        password= getpass("Enter a pwd: ")
    ) as connection:
        print(connection)
    
    query="""
    SELECT id,email,user_id FROM commemoro.users WHERE user_id=3;
    """
    print(query)
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
except Error as e:
      print(e)
