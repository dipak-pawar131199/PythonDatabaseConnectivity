import mysql.connector
# for used database add one more keywords parameter  database in connect() method
Con=mysql.connector.connect(host='localhost',user='root',password='password',Database='emp')
Cursor=Con.cursor()

  
