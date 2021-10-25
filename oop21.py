# Write a OOP program to print following pattern. (hint: nested for/while loop). Input number required no. of lines and pattern character from user.
# @
# @@@
# @@@@@
# @@@@@@@
# @@@@@@@@@
# @@@@@@@@@@@
class Pyramid:
    def __int__(self):
        self.__size=0
    def getInput(self):
        self.__size=int(input("Please enter the Total Number of List Elements: "))
    def halfPyramid(self):
        self.__size=int(input("Please enter the Total Number of List Elements: "))
        for i in range(self.__size):
            for j in range(i+1):
                print(end="* ")
            print()
    def invertedHalfPyramid(self):
        self.__size=int(input("Please enter the Total Number of List Elements: "))
        for i in range(self.__size):
            for j in range(i, self.__size):
                print(end="* ")
            print()
    def fullPyramid(self):
        self.__size=int(input("Please enter the Total Number of List Elements: "))
        for i in range(self.__size):
            for s in range(self.__size, i+1, -1):
                print(end=" ")
            for j in range(i + 1):
                print(end="* ")
            print()
    def invertedFullPyramid(self):
        self.__size=int(input("Please enter the Total Number of List Elements: "))
        for i in range(self.__size):
            for s in range(i):
                print(end=" ")
            for j in range(i, 5):
                print(end="* ")
            print()
r=Pyramid()
while True:
    print("1. Print Half Pyramid of Stars")
    print("2. Print Inverted Half Pyramid of Stars")
    print("3. Print Full Pyramid of Stars")
    print("4. Print Inverted Full Pyramid of Stars")
    print("5. Exit")
    print("Enter Your Choice: ", end="")
    choice = int(input())
    if choice==1:
        r.halfPyramid()
    elif choice==2:
        r.invertedHalfPyramid()
    elif choice==3:
        r.fullPyramid()
    elif choice==4:
        r.invertedFullPyramid()
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Wrong Choice!")
