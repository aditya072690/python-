'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

A program to check whether inputted string is palindrome or not.
Eg Enter a name : liril
Liril is a palindrom
'''

class Palindrome:
    def __int__(self):
        self.String = ''

    def display_Condition(self):

        self.String = input("Enter a string:")

        if (self.String == self.String[::-1]):
            print("The string is a palindrome!")
        else:
            print("The string isn't a palindrome!")


r = Palindrome()
r.display_Condition()
