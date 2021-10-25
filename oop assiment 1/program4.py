'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Program to print binary form a any number using 16 bit representation. (without library function) (You can use list for 16 bit representation)
Eg. Enter any number : 20
0000000000010100
Enter any number -5
1000000000000101
'''

class bin_representation:
    def __init__(self,num):
        self.__string = ''
        self.__num = num

    def convert(self):
        i = 1 << 15
        while (i > 0):

            if ((self.__num & i) != 0):

                self.__string += '1'

            else:
                self.__string += '0'

            i = i // 2
    def display(self):
        print('The 16 bit binary representation of {0} is: {1}'.format(self.__num,self.__string))

run = bin_representation(2)
run.convert()
run.display()