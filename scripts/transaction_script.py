from db_script import MySQLConnector
from mysql.connector import Error
from main_script import MainScript

db = MySQLConnector()
ms = MainScript()

class TransactionSum:
    def sales_summary_all(self):
        lists = ms.display_paper_type()
        print(lists)
        self.display_cost_all()
        self.display_price_all(1)
        self.display_pages_printed_all(1)

    def display_cost_all(self):
        try:
            conn = db.db_connect()
            query = "SELECT cost_per_page FROM tbl_cost;"
            result = db.execute_query(conn, query).fetchall()
            lists = []
            for res in result:
                lists.append(res[0])
            conn.close()
            print(lists)
        except Error as e:
            print(e)

    def display_price_all(self, id_paper):
        try:
            conn = db.db_connect()
            query = f"SELECT price, id_paper FROM tbl_print_cost WHERE id_paper = {id_paper};"
            result = db.execute_query(conn, query).fetchall()
            lists = []
            for res in result:
                lists.append(res[0])
            conn.close()
            print(lists)
        except Error as e:
            print(e)

    def display_pages_printed_all(self, id_paper):
        try:
            conn = db.db_connect()
            query = f"SELECT print_no_page FROM tbl_print as tp INNER JOIN tbl_print_cost as tpc ON tp.id_print_cost = tpc.id_print_cost WHERE tpc.id_paper = {id_paper};"
            result = db.execute_query(conn, query).fetchall()
            lists = []
            for res in result:
                lists.append(res[0])
            conn.close()
            print(lists)
        except Error as e:
            print(e)

TransactionSum().sales_summary_all()
