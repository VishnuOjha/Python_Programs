import mysql.connector as con


def listStudents():

    dbCon = con.connect(host="localhost",user="root",passwd="root",database="pythoncrud")

    listQuery = "select * from student"

    mycur = dbCon.cursor()

    mycur.execute(listQuery)

    std = mycur.fetchall()

    for student in std:
        print(student)

    print(mycur.rowcount)

    dbCon.close()

def serachStduent():

    dbCon  = con.connect(host="localhost",user="root",passwd="root",database="pythoncrud")

    name = input("Enter a name for search")

    searchQuery = "select * from student where name = '"+name+"'"
    value = name

    myCur = dbCon.cursor()

    myCur.execute(searchQuery,value)
    print(searchQuery)


    std1 = myCur.fetchone()

    print(std1)

    dbCon.close()


def deletStudent():
    dbCon = con.connect(host="localhost", user="root", passwd="root", database="pythoncrud")

    name = input("Enter name for delet record : ")
    deletQuery = "delete from student where name='"+name+"'"
    myCur = dbCon.cursor()
    myCur.execute(deletQuery)
    print(myCur.rowcount,"Records deleted")
    dbCon.commit()
    dbCon.close()






#
# listStudents()
# serachStduent()
#updateStudent()
deletStudent()
