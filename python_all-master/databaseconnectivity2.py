'''
import mysql.connector
db=mysql.connector.connect(
 host="localhost",
user="root",
passwd="root",
database= "testdb"
 )
my=db.cursor()
x="INSERT INTO students(name,age).VALUES (%s,%s)"
s1=("parul",20)
my.execute(x,s1)
db.commit()
'''

import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    passwd="root",
    user="root",
    database="testdb"
)
cur = database.cursor()
# cur.execute("CREATE DATABASE testdb" )
# cur.execute("SHOW DATABASE ")
# cur.execute("CREATE TABLE students ")
x = "INSERT INTO students (name,age) VALUES (%s,%s)"
s1 = ("x", 1)
s2 = ("y", 3)
s3 = (
    ("xx", 5),
    ("T", 6),
    ("ss", 55)
)
cur.execute(x, s1)
cur.execute(x, s2)
cur.executemany(x, s3)
cur.execute("SELECT * FROM students")
res = cur.fetchmany()
for i in res:
    print(i)
    database.commit()
    database.close()
