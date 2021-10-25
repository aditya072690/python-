
'''
Write a program for lottery simulation. Generate 6 digit random number. Allow user to input only 6 digit number.
If all the 6 digits matches then user wins 100000,
if 5 digits match in sequence then user wins 85000,
if 4 digits match in sequence then user wins 50000,
if 3 digits matches in sequence then user wins 20000,
if 2 digit matches user wins 2000.
'''
import random
import emoji
import time

class Lottery():

    def __init__(self):
        self.__lotteryNumber = random.randint(100000,999999)
        print(self.__lotteryNumber)
        while True:
            try:
                self.__userNumber = int(input('Please enter your lottery ticket number: '))
                if (len(str(self.__userNumber)) != 6):
                    print('Please enter a valid lottery ticket number: ')
                    continue
                else:
                    pass
            except:
                print("Alphabets or Special characters are not allowed as lottery ticket number.")
            else:
                break

    def lotteryNumberSplit(self):

        self.__lot_dig1 = str((self.__lotteryNumber // 100000) % 10)
        self.__lot_dig2 = str((self.__lotteryNumber // 10000) % 10)
        self.__lot_dig3 = str((self.__lotteryNumber // 1000) % 10)
        self.__lot_dig4 = str((self.__lotteryNumber // 100) % 10)
        self.__lot_dig5 = str((self.__lotteryNumber // 10) % 10)
        self.__lot_dig6 = str(self.__lotteryNumber % 10)

    def userNumberSplit(self):
        self.__dig_1 = str((self.__userNumber // 100000) % 10)
        self.__dig_2 = str((self.__userNumber // 10000) % 10)
        self.__dig_3 = str((self.__userNumber // 1000) % 10)
        self.__dig_4 = str((self.__userNumber // 100) % 10)
        self.__dig_5 = str((self.__userNumber // 10) % 10)
        self.__dig_6 = str(self.__userNumber % 10)

    def numberMatch(self):
        l_number = self.__lotteryNumber
        u_number = self.__userNumber

        l_num_1 = self.__lot_dig1
        l_num_2 = self.__lot_dig2
        l_num_3 = self.__lot_dig3
        l_num_4 = self.__lot_dig4
        l_num_5 = self.__lot_dig5
        l_num_6 = self.__lot_dig6

        num_1 = self.__dig_1
        num_2 = self.__dig_2
        num_3 = self.__dig_3
        num_4 = self.__dig_4
        num_5 = self.__dig_5
        num_6 = self.__dig_6

        #user's number => fives
        uFive1 = int(num_1 + num_2 + num_3 + num_4 + num_5)
        uFive2 = int(num_2 + num_3 + num_4 + num_5 + num_6)
        #lottery's number => fives
        lFive1 = int(l_num_1 + l_num_2 + l_num_3 + l_num_4 + l_num_5)
        lFive2 = int(l_num_2 + l_num_3 + l_num_4 + l_num_5 + l_num_6)

        # user's number => fours
        uFour1 = int(num_1 + num_2 + num_3 + num_4)
        uFour2 = int(num_2 + num_3 + num_4 + num_5)
        uFour3 = int(num_3 + num_4 + num_5 + num_6)
        # lottery's number => fours
        lFour1 = int(l_num_1 + l_num_2 + l_num_3 + l_num_4)
        lFour2 = int(l_num_2 + l_num_3 + l_num_4 + l_num_5)
        lFour3 = int(l_num_3 + l_num_4 + l_num_5 + l_num_6)

        # user's number => threes
        uThree1 = int(num_1 + num_2 + num_3)
        uThree2 = int(num_2 + num_3 + num_4)
        uThree3 = int(num_3 + num_4 + num_5)
        uThree4 = int(num_4 + num_5 + num_6)
        # lottery's number => threes
        lThree1 = int(l_num_1 + l_num_2 + l_num_3)
        lThree2 = int(l_num_2 + l_num_3 + l_num_4)
        lThree3 = int(l_num_3 + l_num_4 + l_num_5)
        lThree4 = int(l_num_4 + l_num_5 + l_num_6)

        # user's number => twos
        uTwo1 = int(num_1 + num_2)
        uTwo2 = int(num_2 + num_3)
        uTwo3 = int(num_3 + num_4)
        uTwo4 = int(num_4 + num_5)
        uTwo5 = int(num_5 + num_6)
        # lottery's number => twos
        lTwo1 = int(l_num_1 + l_num_2)
        lTwo2 = int(l_num_2 + l_num_3)
        lTwo3 = int(l_num_3 + l_num_4)
        lTwo4 = int(l_num_4 + l_num_5)
        lTwo5 = int(l_num_5 + l_num_6)

        for i in range(6):
            time.sleep(1)
            print(".")

        if (l_number == u_number):
            print('Congrats!!! You Have won Rupees 1,00,000!')
        else:
            if ((uFive1 == lFive1 or uFive1 == lFive2) or (uFive2 == lFive1 or uFive2 == lFive2)):
                print('Congrats!!! You Have won Rupees 85,000!')
            else:
                if ((uFour1 == lFour1 or uFour1 == lFour2 or uFour1 == lFour3) or (uFour2 == lFour1 or uFour2 == lFour2 or uFour2 == lFour3) or (uFour3 == lFour1 or uFour3 == lFour2 or uFour3 == lFour3)):
                    print('Congrats!!! You Have won Rupees 50,000!')
                else:
                    if ((uThree1 == lThree1 or uThree1 == lThree2 or uThree1 == lThree3 or uThree1 == lThree4) or (uThree2 == lThree1 or uThree2 == lThree2 or uThree2 == lThree3 or uThree2 == lThree4) or (uThree3 == lThree1 or uThree3 == lThree2 or uThree3 == lThree3 or uThree3 == lThree4) or (uThree4 == lThree1 or uThree4 == lThree2 or uThree4 == lThree3 or uThree4 == lThree4)):
                        print('Congrats!!! You Have won Rupees 20,000!')
                    else:
                        if ((uTwo1 == lTwo1 or uTwo1 == lTwo2 or uTwo1 == lTwo3 or uTwo1 == lTwo4 or uTwo1 == lTwo5) or (uTwo2 == lTwo1 or uTwo2 == lTwo2 or uTwo2 == lTwo3 or uTwo2 == lTwo4 or uTwo2 == lTwo5) or (uTwo3 == lTwo1 or uTwo3 == lTwo2 or uTwo3 == lTwo3 or uTwo3 == lTwo4 or uTwo3 == lTwo5) or (uTwo4 == lTwo1 or uTwo4 == lTwo2 or uTwo4 == lTwo3 or uTwo4 == lTwo4 or uTwo4 == lTwo5) or (uTwo5 == lTwo1 or uTwo5 == lTwo2 or uTwo5 == lTwo3 or uTwo5 == lTwo4 or uTwo5 == lTwo5)):
                            print('Congrats!!! You Have won Rupees 2,000!')
                        else:
                            print(emoji.emojize("Sorry!!! You didn't win! Better Luck Next Time :thumbs_up: :thumbs_up: "))
r = Lottery()
r.lotteryNumberSplit()
r.userNumberSplit()
r.numberMatch()













"""
import random
import emoji

class Lottery:
    def __init__(self):
        self.__random_num = random.randint(100000, 1000000)
        print("Random Number : ", self.__random_num)
        while True:
            try:
                self.__user_num = int(input('Please enter your lottery ticket number: '))
                if (len(str(self.__user_num)) != 6):
                    print('Please enter a valid lottery ticket number: ')
                    continue
                else:
                    pass
            except:
                print("Alphabets or Special characters are not allowed as lottery ticket number.")
            else:
                break
        #self.__user_num = int(input("Enter 6 digit Number : "))
        self.__list_random = []
        self.__list_user_win_num = []

    def lottry_num_list(self):
        while (self.__random_num > 0):

            remainder = self.__random_num % 10
            self.__list_random.append(remainder)
            self.__random_num = self.__random_num // 10
        self.__list_random.reverse()


    def user_num_list(self):
        revs_number = 0
        while (self.__user_num > 0):
            # Logic
            remainder = self.__user_num % 10
            self.__list_user_win_num.append(remainder)
            self.__user_num = self.__user_num // 10

        self.__list_user_win_num.reverse()
        #print("Random Num : ", self.__list_user_win_num)

    def wining_price(self):
        if(self.__list_random == self.__list_user_win_num):
            print("Congrats!!! You Have won Rupees 1,00,000")
        else:
            if((self.__list_random[0:5] == self.__list_user_win_num[0:5] or self.__list_random[0:5] == self.__list_user_win_num[1:6]) or (self.__list_random[1:6] == self.__list_user_win_num[0:5] or self.__list_random[1:6] == self.__list_user_win_num[1:6])):
                print("Congrats!!! You Have won Rupees 85,000")
            else:
                if((self.__list_random[0:4] == self.__list_user_win_num[0:4] or self.__list_random[0:4] == self.__list_user_win_num[1:5] or self.__list_random[0:4] == self.__list_user_win_num[2:6]) or (self.__list_random[1:5] == self.__list_user_win_num[0:4] or self.__list_random[1:5] == self.__list_user_win_num[1:5] or self.__list_random[1:5] == self.__list_user_win_num[2:6]) or (self.__list_random[2:6] == self.__list_user_win_num[0:4] or self.__list_random[2:6] == self.__list_user_win_num[1:5] or self.__list_random[2:6] == self.__list_user_win_num[2:6])):
                    print("Congrats!!! You Have won Rupees 50,000")
                else:
                    if((self.__list_random[0:3] == self.__list_user_win_num[0:3] or self.__list_random[0:3] == self.__list_user_win_num[1:4] or self.__list_random[0:3] == self.__list_user_win_num[2:5] or self.__list_random[0:3] == self.__list_user_win_num[3:6]) or (self.__list_random[1:4] == self.__list_user_win_num[0:3] or self.__list_random[1:4] == self.__list_user_win_num[1:4] or self.__list_random[1:4] == self.__list_user_win_num[2:5] or self.__list_random[1:4] == self.__list_user_win_num[3:6]) or (self.__list_random[2:5] == self.__list_user_win_num[0:3] or self.__list_random[2:5] == self.__list_user_win_num[1:4] or self.__list_random[2:5] == self.__list_user_win_num[2:5] or self.__list_random[2:5] == self.__list_user_win_num[3:6]) or (self.__list_random[3:6] == self.__list_user_win_num[0:3] or self.__list_random[3:6] == self.__list_user_win_num[1:4] or self.__list_random[3:6] == self.__list_user_win_num[2:5] or self.__list_random[3:6] == self.__list_user_win_num[3:6])):
                        print("Congrats!!! You Have won Rupees 20,000")
                    else:
                        if((self.__list_random[0:2] == self.__list_user_win_num[0:2] or self.__list_random[0:2] == self.__list_user_win_num[1:3] or self.__list_random[0:2] == self.__list_user_win_num[2:4] or self.__list_random[0:2] == self.__list_user_win_num[3:5] or self.__list_random[0:2] == self.__list_user_win_num[4:6]) or (self.__list_random[1:3] == self.__list_user_win_num[0:2] or self.__list_random[1:3] == self.__list_user_win_num[1:3] or self.__list_random[1:3] == self.__list_user_win_num[2:4] or self.__list_random[1:3] == self.__list_user_win_num[3:5] or self.__list_random[1:3] == self.__list_user_win_num[4:6]) or (self.__list_random[2:4] == self.__list_user_win_num[0:2] or self.__list_random[2:4] == self.__list_user_win_num[1:3] or self.__list_random[2:4] == self.__list_user_win_num[2:4] or self.__list_random[2:4] == self.__list_user_win_num[3:5] or self.__list_random[2:4] == self.__list_user_win_num[4:6]) or (self.__list_random[3:5] == self.__list_user_win_num[0:2] or self.__list_random[3:5] == self.__list_user_win_num[1:3] or self.__list_random[3:5] == self.__list_user_win_num[2:4] or self.__list_random[3:5] == self.__list_user_win_num[3:5] or self.__list_random[3:5] == self.__list_user_win_num[4:6]) or (self.__list_random[4:6] == self.__list_user_win_num[0:2] or self.__list_random[4:6] == self.__list_user_win_num[1:3] or self.__list_random[4:6] == self.__list_user_win_num[2:4] or self.__list_random[4:6] == self.__list_user_win_num[3:5] or self.__list_random[4:6] == self.__list_user_win_num[4:6])):
                            print("Congrats!!! You Have won Rupees 2,000")
                        else:
                            print(emoji.emojize("Sorry!!! You didn't win! Better Luck Next Time :thumbs_up: :thumbs_up: "))


a = Lottery()
a.lottry_num_list()
a.user_num_list()
a.wining_price()
"""