import mysql.connector
Con=mysql.connector.connect(host='localhost',user='root',password='password', Database='emp')
Cursor=Con.cursor() 
Cursor.execute("desc emp")
for i in Cursor:
   print (i)

