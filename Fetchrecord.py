import mysql.connector
Con=mysql.connector.connect(host='localhost',user='root',password='password',Database='emp')
Cursor=Con.cursor() 
# fetching records by fetchall()
Cursor.execute('select * from emp')
# fetchall () used to fetch all row from table
Result=Cursor.fetchall()
for i in Result:
  print(i)
# for fetch single row used method fetchone() and it return first row of result
result=Cursor.fetchone()
print(result)
