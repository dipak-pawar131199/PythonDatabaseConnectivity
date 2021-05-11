import mysql.connector
Con=mysql.connector.connect(host='localhost',user='root',password='password',Database='emp')
Cursor=Con.cursor()
Cursor.execute("create table emp(eid int primary key,ename varchar(20),sal int")

