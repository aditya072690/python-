'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write an OOP to calculate exponent from inputted base and power value.

Eg. Enter a base value : 3

Enter a power value : 4

For base 3 and power 4, the answer is 81
'''

class exponent:

    def init(self):
        self.__num = 0

    def get_number(self, value):
        self.__num = value

    def display(self):
        print("The Answer for entered input is {0}".format(self.__num))

    def calculate(self, object):
        solution = exponent()
        solution.__num = self.__num ** object.__num
        return solution


base = exponent()
base.get_number(5)
power = exponent()
power.get_number(2)
solution = base.calculate(power)
solution.display()