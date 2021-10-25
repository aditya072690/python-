# Write a OOP program to print following pattern. (hint: nested for/while loop). Input number required no. of lines and pattern character from user.
#            @
#           @@@
#          @@@@@
#         @@@@@@@
#        @@@@@@@@@
#       @@@@@@@@@@@
class Pyramid:
    def __int__(self):
        self.__size=0
    def fullPyramid(self):
        self.__size=int(input("Please enter the number to print a Pyramid: "))
        for i in range(self.__size):
            for s in range(self.__size, i+1, -1):
                print(end=" ")
            for j in range(i + 1):
                print(end="* ")
            print()

print("Print Full Pyramid of Stars")
r=Pyramid()
r.fullPyramid()
