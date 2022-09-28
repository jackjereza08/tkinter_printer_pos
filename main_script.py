from getpass import getpass
import mysql.connector as connector
from mysql.connector import Error
from datetime import datetime, date


class MainScript:
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
            if result == None:
                return "0"
            conn.close()

            return result
        except Error as e:
            print(e)

    def show_print_price(self, index, type):
        try:
            conn = self.db_connect()
            query = f"SELECT price from tbl_print_cost WHERE id_paper = {index+1} AND print_type = '{type}'"
            result = self.execute_query(conn, query).fetchone()
            if result == None:
                return "0.00"
            conn.close()

            return result
        except Error as e:
            print(e)

    def calculate(self, price, no_pages):
        return price * no_pages

    def save_transaction(self, id_paper, print_type, print_price, print_no_page):
        print_date = datetime.now()
        
        try:
            conn = self.db_connect()
            query = f"""
                    INSERT INTO tbl_print(id_paper,print_type,print_price,print_no_page,print_date)
                    VALUES
                    ({id_paper},"{print_type}",{print_price},{print_no_page},'{print_date.date()}');
                    """
            result = self.execute_query(conn, query)
            conn.commit()
            conn.close()

            return result.rowcount
        except Error as e:
            print(e)

