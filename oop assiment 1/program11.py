'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write a OOP program to find Euclidean Distance.
'''
class Point:

    def __init__(self):
        self.__x1 = 0
        self.__y1 = 0
        self.__x2 = 0
        self.__y2 = 0
        self.__delta_x = 0
        self.__delta_y =  0
        self.__euDist = 0

    def get_input(self):
        self.__x1 = int(input('Please enter integer value for x1: '))
        self.__y1 = int(input('Please enter integer value for y1: '))
        self.__x2 = int(input('Please enter integer value for x2: '))
        self.__y2 = int(input('Please enter integer value for y2: '))

    def dist_to_point(self):
        self.__delta_x = self.__x2 - self.__x1
        self.__delta_y = self.__y2 - self.__y1
        self.__euDist = (self.__delta_x ** 2 + self.__delta_y ** 2) ** 0.5
        return self.__euDist

    def display(self):
        print("The Euclidean distance is: ",self.__euDist)

run = Point()
run.get_input()
run.dist_to_point()
run.display()