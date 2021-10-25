'''
@author: 20124051 Aditya Chauhan
@description: Program No. -
Write an Object Oriented program to accept two numbers and one mathematical operator. Using Operator Overloading technique, calculate and display appropriate answer. (Implement for +,-,*, //, = = and < operators)
example output:
Enter first number : 45
Enter mathematical operator : + Enter second number : 60
45 + 60 = 105
'''

class Calculator():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def __add__(self,num2):
        return self.num1 + self.num2
    def __sub__(self,num2):
        return self.num1 - self.num2
    def __mul__(self,num2):
        return self.num1 * self.num2
    def __floordiv__(self,num2):
        return self.num1 // self.num2
    def __eq__(self,num2):
        return self.num1 == self.num2
    def __len__(self,num2):
        return self.num1 < self.num2

num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
obj=Calculator(num1,num2)
while True:
    def menu():
        opreration = ("1. Add= + \n2. Sub= - \n3. Multiply= * \n4. Divide= // \n5.Equal= == \n6. Less-Than= <")
        print(opreration)
    menu()
    choice = input('Select an operator : ')

    if choice == '+':
        print("Result: ",obj.__add__(num2))
    elif choice == '-':
        print("Result: ",obj.__sub__(num2))
    elif choice == '*':
        print("Result: ",obj.__mul__(num2))
    elif choice == '//':
        print("Result: ",obj.__floordiv__(num2))
    elif choice == '==':
        print("Result: ",obj.__eq__(num2))
    elif choice == '<':
        print("Result: ",obj.__len__(num2))
        break

    else:
        print('Invalid option')
        break
    break

# class Calculator:
#     def __init__(self):
#         self.__num_1 = int(input('Please enter number 1: '))
#         self.__operator = input('Please enter mathematical operator: ')
#         self.__num_2 = int(input('Please enter number 2: '))
#
#     def calculate(self):
#         self.__calculation = 0
#         self.__opName = ''
#         if self.__operator == '+':
#             self.__calculation = self.__num_1 + self.__num_2
#             self.__opName = 'Addition'
#         elif self.__operator == '-':
#             self.__calculation = self.__num_1 - self.__num_2
#             self.__opName = 'Subtraction'
#         elif self.__operator == '*':
#             self.__calculation = self.__num_1 * self.__num_2
#             self.__opName = 'Multiplication'
#         elif self.__operator == '/':
#             self.__calculation = self.__num_1 / self.__num_2
#             self.__opName = 'Division'
#         elif self.__operator=='<':
#             self.__calculation=self.__num_1 < self.__num_2
#             self.__opName='less than'
#         elif self.__operator=='//':
#             self.__calculation=self.__num_1//self.__num_2
#             self.__opName='floor divison'
#
#
#     def display(self):
#         print('The {0} of {1} and {2} is {3}.'.format(self.__opName,self.__num_1,self.__num_2,self.__calculation))
#
# run = Calculator()
# run.calculate()
# run.display()