'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write a program which inputs a number. Display that number in word format.
Eg.
459 – Four Five Nine
7091 – Seven Zero Nine One
26 - Two Six
'''

class Word_Format:

    def __init__(self):
        self.__digit = input('Please enter a number: ')


    def printValue(self, number):
        if number == '0':
            print("Zero ")

        elif number == '1':
            print("One ")

        elif number == '2':
            print("Two ")

        elif number == '3':
            print("Three")

        elif number == '4':
            print("Four ")

        elif number == '5':
            print("Five ")

        elif number == '6':
            print("Six ")

        elif number == '7':
            print("Seven")

        elif number == '8':
            print("Eight")

        elif number == '9':
            print("Nine ")

    def printWord(self):
        i = 0
        num = self.__digit
        length = len(num)


        while i < length:
            self.printValue(num[i])
            i += 1
run = Word_Format()
run.printWord()
