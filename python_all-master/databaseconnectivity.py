import mysql.connector
db=mysql.connector.connect(
 host="localhost",
user="root",
passwd="root",
database="testdb"
 )

my=db.cursor()
#mycursor.execute("CREATE DATABASE testdb")
#my.execute("SHOW DATABASES")
my.execute("CREATE TABLE students (name VARCHAR(233),age INTEGER(10))")
#for i in my:
 #   print(i)