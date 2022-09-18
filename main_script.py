from getpass import getpass
import mysql.connector as connector

conn = connector.connect(
        host='localhost',
        user= input("Username:"),
        passwd=getpass("Password:"))

cursor = conn.cursor()
create_database = "CREATE DATABASE print_pos"
cursor.execute(create_database)

print(conn)
print(cursor.execute("SHOW DATABASES"))

conn.close()

