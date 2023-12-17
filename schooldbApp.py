import pymysql.cursors
from datetime import datetime
import process as pro
print("What do you want to do")
print("\n")
print("1)Add a student")
print("2)find student")
print("3)Update student infos")
print("4)Delete student")
print("\n")
process=int(input("Whats your process:"))
if process == 2:
    stnum=input("enter student'S number:")
    pro.select(stnum)
if process==1:
    stnum2=int(input("enter student's number:"))
    stname=input("enter student's name:")
    stsnum=input("enter student's surname:")
    stbd1=int(input("enter student's birth-day:"))
    stbd2=int(input("enter student's birth-month:"))
    stbd3=int(input("enter student's birth-year:"))
    stbd=datetime(stbd3,stbd2,stbd1)
    stgender=input("enter student's gender(E(Man)/K(Women)):")
    pro.insert(stnum2,stname,stsnum,stbd,stgender)
if process==3:
    stnum4=int(input("please enter student's number who you want to change:"))
    pro.update(stnum4)
if process==4:
    stnum5=int(input("please enter student's number who you want to delete:"))
    pro.delete(stnum5)
else:
    print("wrong choice selected")