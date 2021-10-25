'''
Write an Object Oriented Program which performs CRUD with Students Table (rollno,name,weight)
created in MySQL Database.
'''
import mysql.connector
import sys
def displayAll():
    mydb = mysql.connector.connect(host="localhost",user="root",password="adityA@123",database="dbtest")
    myc=mydb.cursor()
    try:
        myc.execute("select * from db")
        rs=myc.fetchall()
        for row in rs:
            print(row)
    except:
        print("Unable to fetch data")
    mydb.close()

def searchStudent():
    sval=input("Enter enrollment id to search the reccord:")
    mydb = mysql.connector.connect(host="localhost",user="root",password="adityA@123",database="dbtest")
    myc=mydb.cursor()
    try:
        myc.execute("select * from db where EnrolmentId='"+sval+"'")
        rs=myc.fetchall()
        for row in rs:
            print(row)
    except:
        print("Unable to fetch data")
    mydb.close()

def addStudent():
    mydb = mysql.connector.connect(host="localhost",user="root",password="adityA@123",database="dbtest")
    myc=mydb.cursor()
    enoid=input("Enter Enrolllment ID:")
    fn=input("Enter First Name:")
    ln=input("Enter Last Name:")
    mno=input("Enter mobil number:")
    try:
        myc.execute("Insert into db(EnrolmentId,FirstName,LastName,MobileNo)"+
                    "values('"+enoid+"','"+fn+"','"+ln+"','"+mno+"')")
        mydb.commit()
        print("Record Added Succesfully")
    except:
        mydb.rollback()
        print("Issues in Transaction, Failed Transaction Rollbacked")
    mydb.close()

def updateStudent():
    mydb = mysql.connector.connect(host="localhost",user="root",password="adityA@123",database="dbtest")
    myc=mydb.cursor()
    enoid=input("Enter Enrolllment ID:")
    fn=input("Enter First Name:")
    ln=input("Enter Last Name:")
    mno=input("Enter mobil number:")
    try:
        myc.execute("update db set FirstName='"+fn+"',LastName='"+ln+"',MobileNo='"+mno+"' where EnrolmentId='"+enoid+"'")
        mydb.commit()
        print("Record Updated Succesfully")
    except:
        mydb.rollback()
        print("Unable to update record")
    mydb.close()

def deleteStudent():
    sval=input("Enter enrollment id to DELETE the reccord:")
    mydb = mysql.connector.connect(host="localhost",user="root",password="adityA@123",database="dbtest")
    try:
        myc=mydb.cursor()
        myc.execute("delete from db where EnrolmentId='"+sval+"'")
        mydb.commit()
        print("Data Deleted Successfully")
    except:
        mydb.rollback()
    mydb.close()

while(1):
    print("######## M E N U #########")
    print("1. Display All")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("0. EXIT")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        displayAll()
    elif(choice==2):
        searchStudent()
    elif(choice==3):
        addStudent()
    elif(choice==4):
        updateStudent()
    elif(choice==5):
        deleteStudent()
    elif(choice==0):
        sys.exit(0)
