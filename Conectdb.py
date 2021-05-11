import mysql.connector
Con=mysql.connector.connect(host='localhost',user='root',password='password')
Cursor=Con.cursor() # used for executing SQL queries
SQL=" create database emp"
Cursor.execute(SQL) # execute () is used to execute SQL statements
print ("database created")

