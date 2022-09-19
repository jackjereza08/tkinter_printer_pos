from getpass import getpass
import mysql.connector as connector
from mysql.connector import Error


class Main_Script:
    def __init__(self):
        try:
            conn = self.db_connect()
            query = "SELECT * from tbl_paper"
            result = self.execute_query(conn, query).fetchall()
            for x in result:
                print(x)
            conn.close()
        except Error as e:
            print(e)

    def db_connect(self):
        conn = connector.connect(
            host='localhost',
            user= 'root',
            passwd='root',
            database='db_print_pos')      
        return conn

    def execute_query(self, conn, query):
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor


    def display_paper_type(self):
        try:
            db_connect()
            self.cursor.execute()
        except Error as e:
            print(e)

Main_Script()
