from getpass import getpass
import mysql.connector as connector
from mysql.connector import Error


class Main:
    def __init__(self):
        try:
            conn = connector.connect(
                    host='localhost',
                    user= input("Username:"),
                    passwd=getpass("Password:"))

            cursor = conn.cursor()
            create_database = "CREATE DATABASE db_print_pos"
            cursor.execute(create_database)

            print(conn)
            print(cursor.execute("SHOW DATABASES"))

            conn.close()
        except Error as e:
            print(e)

Main()

