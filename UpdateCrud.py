import mysql.connector as con


def updateStudent():
    dbCon = con.connect(host="localhost", user="root", passwd="root", database="pythoncrud")
    myCur = dbCon.cursor()
    name = input("Enter a name for update")
    value = name
    selectQuery = "select * from student where name ='"+name+"'"

    myCur.execute(selectQuery,value)
    std1 = myCur.fetchone()
    print(std1)
    print("--------------Update Record---------------")
    name = input("Enter a name :")
    age = input("Enter a age :")
    gender = input("Enter gender :")

    updateQuery = "update student set name='"+name+"',age='"+age+"',gender='"+gender+"'"

    myCur.execute(updateQuery)

    dbCon.commit()

    dbCon.close()

updateStudent()