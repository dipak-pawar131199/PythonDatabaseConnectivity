import mysql.connector
Con=mysql.connector.connect(host='localhost',user='root',password='password', Database='emp')
Cursor=Con.cursor() 
SQL='insert into emp values(1,'Rakesh',10000)'
try:
   Cursor.execute(SQL)
   Con.commit() # save changes in database
except Exception  as e:
  Con.rollback() # rollback transection
  print(e)
finally:
  # remove all resources acquired by cursor and con
  Cursor.close()
  Con.close()
