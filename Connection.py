# import mysqlconnector
import mysql.connector
Con=mysql.connector.connect(host='localhost',user='root',password='password')
Cursor=Con.cursor()
