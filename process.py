import pymysql.cursors
from datetime import datetime
def insert(number,name,surname,birth,gender):
    mydb=pymysql.connect(
        host="localhost",
        user="root",
        password="34.bjkberat",
        database="schooldb"
    )
    mycursor=mydb.cursor()
    sql="INSERT INTO students(Student_Number,Student_Name,Student_Surname,Student_Birthdate,Student_Gender) VALUE(%s,%s,%s,%s,%s)"
    values=(number,name,surname,birth,gender)
    mycursor.execute(sql,values)
    try:
        print("operating successful")
        mydb.commit()
    except pymysql.connect.Error as err:
        print("ERROR CODE:",err)
    finally:
        mydb.close()
        print("Database closed")
        
        
def select(number1):
    mydb=pymysql.connect(
        host="localhost",
        user="root",
        password="34.bjkberat",
        database="schooldb"
    )
    mycursor=mydb.cursor()
    sql="SELECT * FROM students WHERE Student_Number=%s"
    value=number1
    mycursor.execute(sql,value)
    result=mycursor.fetchall()
    for i in result:
        print(f"Student name:{i}")
    try:
        print("operating successful")
        mydb.commit()
    except pymysql.connect.Error as err:
        print("ERROR CODE:", err)
    finally:
        print("Database closed")
        mydb.close()

def update(val):
    mydb=pymysql.connect(
        host="localhost",
        user="root",
        password="34.bjkberat",
        database="schooldb"
    )
    mycursor=mydb.cursor()
    print("Which process you want to make")
    print("1)Update Student's number")
    print("2)Update student's name")
    print("3)Update student's surname")
    print("4)Update student's birtdate")
    print("5)Update student's gender")
    karar=int(input("what's your choice:"))
    if karar==1:
        stnum3=int(input("please enter student's new number:"))
        sql="UPDATE students SET Student_Number=%s where Student_Number=%s  "
        values=(stnum3,val)
        mycursor.execute(sql,values)
        try:
            print("operating successful")
            mydb.commit()
        except pymysql.connect.Error as err:
            print("ERROR CODE:",err)
        finally:
            print("Database closed")
            mydb.close()
    if karar==2:
        stname2=input("please enter student's new name:")
        sql="UPDATE students SET Student_Name=%s where Student_Number=%s "
        values=(stname2,val)
        mycursor.execute(sql,values)
        try:
            print("operating successful")
            mydb.commit()
        except pymysql.connect.Error as err:
            print("ERROR CODE:",err)
        finally:
            print("Database closed")
            mydb.close()
    if karar==3:
        stsnum2=input("please enter student's new surname:")
        sql="UPDATE students SET Student_Surname=%s where Student_Number=%s "
        values=(stsnum2,val)
        mycursor.execute(sql,values)
        try:
            print("operating successful")
            mydb.commit()
        except pymysql.connect.Error as err:
            print("ERROR CODE:",err)
        finally:
            print("database closed")
            mydb.close()
    if karar==4:
        bday=int(input("please enter student's new birth-day:"))
        bmonth=int(input("please enter student's new birth-month:"))
        byear=int(input("please enter student's new birth-year:"))
        newbd=datetime(byear,bmonth,bday)
        sql="UPDATE students SET Student_Birthdate=%s where Student_Number=%s  "
        values=(newbd,val)
        mycursor.execute(sql,values)
        try:
            print("operating successful")
            mydb.commit()
        except pymysql.connect.Error as err:
            print("ERROR CODE:",err)
        finally:
            print("Database closed ")
            mydb.close()
    if karar==5:
        stgender2=input("enter student's gender(E(Man)/K(Women)):")
        sql="UPDATE students SET Student_Gender=%s where Student_Number=%s "
        values=(stgender2,val)
        mycursor.execute(sql,values)
        try:
            print("operating successful")
            mydb.commit()
        except pymysql.connect.Error as err:
            print("ERROR CODE:",err)
        finally:
            print("Database closed")
            mydb.close()
            
def delete(val2):
    mydb=pymysql.connect(
        host="localhost",
        user="root",
        password="34.bjkberat",
        database="schooldb"
    )
    mycursor=mydb.cursor()
    sql="DELETE FROM students WHERE Student_Number=%s"
    values=val2
    mycursor.execute(sql,values)
    
    try:
        print("operating successful")
        mydb.commit()
    except pymysql.connect.Error as err:
        print("ERROR CODE:",err)
    finally:
        print("database closed")
        mydb.close()
    