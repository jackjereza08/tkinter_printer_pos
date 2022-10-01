from db_script import MySQLConnector
from mysql.connector import Error
from datetime import datetime

db = MySQLConnector()

class MainScript:
    def display_paper_type(self):
        try:
            conn = db.db_connect()
            query = "SELECT * from tbl_paper"
            result = db.execute_query(conn, query).fetchall()
            paper_list = []
            for rows in result:
                paper_list.append(rows[1]+" ("+rows[2]+")")
            conn.close()

            return paper_list
        except Error as e:
            print(e)


    def show_available_no_paper(self, paper_index):
        try:
            conn = db.db_connect()
            query = f"SELECT paper_available from tbl_paper WHERE id_paper = {paper_index+1}"
            result = db.execute_query(conn, query).fetchone()
            if result == None:
                return "0"
            conn.close()

            return result
        except Error as e:
            print(e)

    def show_print_price(self, index, type):
        try:
            conn = db.db_connect()
            query = f"SELECT price from tbl_print_cost WHERE id_paper = {index+1} AND print_type = '{type}'"
            result = db.execute_query(conn, query).fetchone()
            if result == None:
                return "0.00"
            conn.close()

            return result
        except Error as e:
            print(e)

    def calculate(self, price, no_pages):
        return price * no_pages

    def save_transaction(self, id_paper, print_type, print_no_page):
        print_date = datetime.now()
        
        try:
            conn = db.db_connect()

            id_print_cost_query = f"""
                        SELECT id_print_cost FROM tbl_print_cost WHERE id_paper = {id_paper} AND print_type = '{print_type}';
                    """
            id_print_cost = db.execute_query(conn, id_print_cost_query).fetchone()
            query = f"""
                    INSERT INTO tbl_print(id_print_cost,print_no_page,print_date)
                    VALUES
                    ({id_print_cost[0]},{print_no_page},'{print_date}');
                    """
            result = db.execute_query(conn, query)
            conn.commit()
            conn.close()

            return result.rowcount
        except Error as e:
            print(e)

