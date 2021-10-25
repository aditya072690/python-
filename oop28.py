# Write an Object Oriented Program which imitates Banking Transaction for a Saving account on an ATM machine.
# Store BankCustomer details permanently in a file. The Software is operated by a Bank Customer through an ATM.
# After entering username and password(instead of card and pin), customer is allowed to view his details,
# Change his pin number, withdraw, deposit into the account. He must be able to transfer amount from his account
# to other also.

import json
import sys
import datetime
import os

class Account():

    def __init__(self):
        self.__name = None
        self.__username = None
        self.__contact = None
        self.__password = None
        self.__pin = None
        self.__balance = None
        self.__withdrawal = None
        self.__deposit = None
        self.__newbalance=None

    def welcome(self):
        print("Welcome to Bank of Chutiya College!!!")
        print("Are you a New Customer (yes) or Are you an Existing Customer (no)")
        while True:
            try:
                temp1 = input()
            except:
                print("Please enter a valid response!!!")
                continue
            else:
                if (temp1 == 'Yes' or temp1 == 'YES' or temp1 == 'yes'):
                    r.getDetails()
                    break
                elif (temp1 == 'No' or temp1 == 'NO' or temp1 == 'no'):
                    r.newCustomer()
                    break
                else:
                    print("Please enter a valid response!!!")
                    continue

    def getDetails(self):
        self.__name = input('Please enter your name: ')
        self.__username = input('Please set a username for your Bank Account: ')

        while True:
            try:
                self.__contact = int(input('Please enter your contact number: '))
            except:
                print('Please enter a valid contact number!!!')
            else:
                if (len(str(self.__contact)) != 10):
                    print("Please enter a valid contact number!!!")
                    continue
                else:
                    break

        while True:
            try:
                self.__password = input('Please set a password (Password must contain one upper case, one lowercase and one digit):')
            except:
                print("Please enter a valid password!!!")

            else:

                for i in self.__password:

                    if i.isdigit():
                        temp2 = True
                    else:
                        temp2 =False
                    if i.isupper():
                        temp3 = True
                    else:
                        temp3 =False
                    if i.islower():
                        temp4 = True
                    else:
                        temp4 =False

                    if (temp2 == True and temp3 == True and temp4 == True):
                        temp_confirm = input('Please confirm the password')
                        if (self.__password == temp_confirm):
                            break
                        else:
                            print("Passwords do not match!!!")
                            continue
                    else:
                        print("Please create a password which fulfills the following conditions:-")
                        print("One Uppercase letter.\nOne Lowercase letter.\nOne digit.")
                        continue

            while True:
                try:
                    self.__pin = int(input('Please enter a four digit pin code'))
                except:
                    print('Please enter a valid pin!!!')
                else:
                    if (len(str(self.__pin)) != 4):
                        print('Please create a four digit pin!!!')
                        continue
                    else:
                        break

            print('Would you like to deposit any money now? (Yes / No)')
            while True:
                try:
                    deposit_bool = input()
                except:
                    print('Please enter a valid input!!!')
                else:
                    if (deposit_bool == 'Yes' or deposit_bool == 'YES' or deposit_bool == 'yes'):
                        while True:
                            try:
                                self.__deposit = int(input('Please enter the Amount'))
                            except:
                                print('Please enter a valid Amount!!!')
                            else:
                                print('An amount of Rs. {0} has been deposited to your Account.'.format(self.__deposit))
                                self.__balance = self.__deposit
                                break
                    elif (deposit_bool == 'No' or deposit_bool == 'NO' or deposit_bool == 'no'):
                        self.__balance = 0
                        break


    def newCustomer(self):
        print("A very warm welcome to the Bank of Chutiya College!")
        print("Please fill out the following details.")

        self.__username = input("Please enter username:")
        self.__userfile = self.__username+'.txt'

    def depositcash(self):
        self.__deposit=float(input("Please enter amount to be deposited:"))
        # filename = self.__username+'.txt'
        transactionfilename = self.__username + '_transactionhistory.txt'
        transactionfile = open(transactionfilename, 'a')
        file = open(self.__userfile, 'a')
        self.__balance = 0
        self.__newbalance = 0
        with open(self.__userfile, 'r') as file:
            for i in file:
                self.__balance = float(i)
        with open(self.__userfile, 'w+') as file2:
            self.__newbalance = self.__balance + self.__deposit
            self.__newbalance = str(self.__newbalance)
            file2.write(self.__newbalance)
            print('Your new balance is:', self.__newbalance)
        with open(transactionfilename, 'a') as file3:
            self.__balance = str(self.__balance)
            self.__deposit = str(self.__deposit)
            file3.write(str(datetime.datetime.now()))
            file3.write(
                '\nPrevious balance: ' + self.__balance + '. Deposit amount is:' + self.__deposit + '. New balance:' + self.__newbalance + '\n')
        file.close()

    def withdrawalcash(self):
        self.__withdrawal = float(input('Please enter amount to be withdrawn:'))
        transactionfilename = self.__username + '_transactionhistory.txt'
        transactionfile = open(transactionfilename, 'a')
        file = open(self.__userfile, 'a')
        self.__balance = 0
        self.__newbalance = 0

        with open(self.__userfile, 'r') as file:
            for i in file:
                self.__balance = float(i)
        with open(self.__userfile, 'w+') as file2:
            if self.__withdrawal > self.__balance:
                print('You have insufficient balance. Your balance is:', self.__balance)
            else:
                self.__newbalance = self.__balance - self.__withdrawal
                self.__newbalance = str(self.__newbalance)
                file2.write(self.__newbalance)
                print('Your new balance is:', self.__newbalance)
                with open(transactionfilename, 'a') as file3:
                    self.__balance = str(self.__balance)
                    self.__withdrawal = str(self.__withdrawal)
                    file3.write(str(datetime.datetime.now()))
                    file3.write(
                        '\nPrevious balance: ' + self.__balance + '. Withdrawn amount is:' +self.__withdrawal + '. New balance:' + self.__newbalance + '\n')
        file.close()

# cust_profile = open('cust_profile.txt','r')
# data = cust_profile.read()
r=Account()
r.welcome()
op = int(input("Do you want to continue? Enter 0 to continue, 1 to Terminate:"))
while True:
    if (op == 0):
        print('What would you like to do today? \n1. Deposit Money\n2. Withdraw Money')
        tp = int(input("eEnter your choice:"))
        if(tp == 1):
            r.depositcash()
        elif(tp == 2):
            r.withdrawalcash()
        elif(tp == 3):
            pass
        else:
            print("Wrong Option")
            op = int(input("Do you want to continue? Select 0 to continue, 1 to Terminate:"))
    elif(op == 1):
        print("GoodBye!")
    else:
        print("Wrong option")
        op = int(input("Do you want to continue? Select 0 to Continue, 1 to Terminate."))
