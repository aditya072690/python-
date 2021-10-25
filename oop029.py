'''
Write an Object Oriented Program which performs CRUD with Students Table (rollno,name,weight)
created in MySQL Database.
'''
import mysql.connector
import sys

class Students():

    def displayAll(self):
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
    def searchStudent(self):
        pass
r=Students()
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
        r.displayAll()
    elif(choice==2):
        pass
        # searchStudent()
    elif(choice==3):
        pass
        # addStudent()
    elif(choice==4):
        pass
        # updateStudent()
    elif(choice==5):
        pass
        # deleteStudent()
    elif(choice==0):
        sys.exit(0)
