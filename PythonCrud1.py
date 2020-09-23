import mysql.connector as con

dbcon = con.connect(host="localhost",user="root",passwd="root",database="pythoncrud")


print(dbcon)


cur = dbcon.cursor()

#cur.execute("CREATE TABLE student (name varchar(20),age int,gender varchar(20))")

cur.execute("insert into student(name,age,gender) value('sakura',20,'female')")
cur.execute("insert into student(name,age,gender) value('yamato',21,'male')")
cur.execute("insert into student(name,age,gender) value('sasuke',18,'male')")
cur.execute("insert into student(name,age,gender) value('yuzuki',20,'female')")

dbcon.commit()