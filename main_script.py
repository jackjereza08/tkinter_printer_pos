from getpass import getpass
import mysql.connector as connector
from mysql.connector import Error


class Main_Script:
    # def __init__(self):
    #     pass
        # self.display_paper_type()

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
            conn = self.db_connect()
            query = "SELECT * from tbl_paper"
            result = self.execute_query(conn, query).fetchall()
            paper_list = []
            for rows in result:
                paper_list.append(rows[1]+" ("+rows[2]+")")
            conn.close()

            return paper_list
        except Error as e:
            print(e)


    def show_available_no_paper(self, paper_index):
        try:
            conn = self.db_connect()
            query = f"SELECT beg_no_pages from tbl_inventory WHERE id_paper = {paper_index+1}"
            result = self.execute_query(conn, query).fetchone()
            conn.close()

            return result
            # print(result)
        except Error as e:
            print(e)

