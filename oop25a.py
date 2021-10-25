# Write a program for lottery simulation. Generate 6 digit random number. Allow user to input only 6 digit number.
# If all the 6 digits matches then user wins 100000,
# if 5 digits match in sequence then user wins 85000,
# if 4 digits match in sequence then user wins 50000,
# if 3 digits matches in sequence then user wins 20000,
# if 2 digit matches user wins 2000.

import random
import time
class Lottery:
    def __int__(self):
        self.__lottery_num=0
        self.__user_num=0

    def display_condition(self):
        self.__lottery_num=random.randint(100000,999999)
        print(self.__lottery_num)
    def lottery_prize(self):
        print("Welcome to the Lottery Program!")
        self.__user_num=eval(input("Please enter a six digit number: "))
        print("Calculating Results.")
        for i in range(3):
            time.sleep(1)
            print(".")
            self.__user_numD6=str(self.__user_num%10)
            self.__user_numD5=str((self.__user_num//10)%10)
            self.__user_numD4=str((self.__user_num//100)%10)
            self.__user_numD3=str((self.__user_num//1000)%10)
            self.__user_numD2=str((self.__user_num//10000)%10)
            self.__user_numD1=str((self.__user_num//100000)%10)

            self.__lottery_numD6=str(self.__lottery_num%10)
            self.__lottery_numD5=str((self.__lottery_num//10)%10)
            self.__lottery_numD4=str((self.__lottery_num//100)%10)
            self.__lottery_numD3=str((self.__lottery_num//1000)%10)
            self.__lottery_numD2=str((self.__lottery_num//10000)%10)
            self.__lottery_numD1=str((self.__lottery_num//100000)%10)

            l1=self.__user_numD1
            l2=self.__user_numD2
            l3=self.__user_numD3
            l4=self.__user_numD4
            l5=self.__user_numD5
            l6=self.__user_numD6

            f1=self.__lottery_numD1
            f2=self.__lottery_numD2
            f3=self.__lottery_numD3
            f4=self.__lottery_numD4
            f5=self.__lottery_numD5
            f6=self.__lottery_numD6

        if (self.__lottery_num == self.__user_num):
            print("you won the game prize wins 100000")

        elif int(self.__user_numD1==self.__lottery_numD1 + self.__user_numD2==self.__lottery_numD2 \
                 + self.__user_numD3==self.__lottery_numD3 + self.__user_numD4==self.__lottery_numD4 \
                 + self.__user_numD5==self.__lottery_numD5 or self.__lottery_numD1==self.__user_numD1 \
                 + self.__lottery_numD2==self.__user_numD2 + self.__lottery_numD3==self.__user_numD3 \
                 + self.__lottery_numD4==self.__user_numD4 + self.__lottery_numD5==self.__user_numD5 \
                 or self.__user_numD2==self.__lottery_numD2 + self.__user_numD3==self.__lottery_numD3 \
                 + self.__user_numD4==self.__lottery_numD4 + self.__user_numD5==self.__lottery_numD5 \
                 + self.__user_numD6==self.__lottery_numD6 or self.__lottery_numD2==self.__user_numD2 \
                 + self.__lottery_numD3==self.__user_numD3 + self.__lottery_numD4==self.__user_numD4 \
                 + self.__lottery_numD5==self.__user_numD5 + self.__lottery_numD6==self.__user_numD6) :

            print("5 of your numbers match the lottery. Your reward is $85000!\n")

        elif int(self.__user_numD1==self.__lottery_numD1 + self.__user_numD2==self.__lottery_numD2 \
                 + self.__user_numD3==self.__lottery_numD3 + self.__user_numD4==self.__lottery_numD4 \
                 or self.__lottery_numD1==self.__user_numD1 + self.__lottery_numD2==self.__user_numD2 \
                 + self.__lottery_numD3==self.__user_numD3 + self.__lottery_numD4==self.__user_numD4 \
                 or self.__user_numD2==self.__lottery_numD2+ self.__user_numD3==self.__lottery_numD3 \
                 + self.__user_numD4==self.__lottery_numD4 + self.__user_numD5==self.__lottery_numD5 \
                 or self.__lottery_numD2==self.__user_numD2 + self.__lottery_numD3==self.__user_numD3 \
                 + self.__lottery_numD4==self.__user_numD4 + self.__lottery_numD5==self.__user_numD5 \
                 or self.__user_numD3==self.__lottery_numD3 + self.__user_numD4==self.__lottery_numD4 \
                 + self.__user_numD5==self.__lottery_numD5 + self.__user_numD6==self.__lottery_numD6 \
                 or self.__lottery_numD3==self.__user_numD3 + self.__lottery_numD4==self.__user_numD4 \
                 + self.__lottery_numD5==self.__user_numD5 + self.__lottery_numD6==self.__user_numD6 ) :

            print("4 of your numbers match the lottery. Your reward is $50000!\n")

        elif self.__user_numD1==self.__lottery_numD1 + self.__user_numD2==self.__lottery_numD2 \
                + self.__user_numD3==self.__lottery_numD3 or self.__lottery_numD1==self.__user_numD1 \
                + self.__lottery_numD2==self.__user_numD2 + self.__lottery_numD3==self.__user_numD3 \
                or self.__user_numD2==self.__lottery_numD2+ self.__user_numD3==self.__lottery_numD3 \
                + self.__user_numD4==self.__lottery_numD4 or self.__lottery_numD2==self.__user_numD2 \
                + self.__lottery_numD3==self.__user_numD3 + self.__lottery_numD4==self.__user_numD4 \
                or self.__user_numD3==self.__lottery_numD3 + self.__user_numD4==self.__lottery_numD4 \
                + self.__user_numD5==self.__lottery_numD5 or self.__lottery_numD3==self.__user_numD3 \
                + self.__lottery_numD4==self.__user_numD4 + self.__lottery_numD5==self.__user_numD5 \
                or self.__user_numD4==self.__lottery_numD4 + self.__user_numD5==self.__lottery_numD5 \
                + self.__user_numD6==self.__lottery_numD6 or self.__lottery_numD4==self.__user_numD4 \
                + self.__lottery_numD5==self.__user_numD5 + self.__lottery_numD6==self.__user_numD6:

            print("3 of your numbers match the lottery. Your reward is $20000!\n")

        elif self.__lottery_num==(self.__user_numD1+self.__user_numD2) \
                or self.__lottery_num==(self.__user_numD2+self.__user_numD3) \
                or self.__lottery_num==(self.__user_numD3+self.__user_numD4) \
                or self.__lottery_num==(self.__user_numD4+self.__user_numD5) \
                or self.__lottery_num==(self.__user_numD5+self.__user_numD6):

            print("2 of your numbers match the lottery. Your reward is $2000!\n")

        # elif self.__user_numD1==self.__lottery_numD1 or self.__user_numD2==self.__lottery_numD2 \
        #     or self.__user_numD3==self.__lottery_numD3 or self.__user_numD4==self.__lottery_numD4\
        #     or self.__user_numD5==self.__lottery_numD5 or self.__lottery_numD1==self.__user_numD1 \
        #     or self.__lottery_numD2==self.__user_numD2 or self.__lottery_numD3==self.__user_numD3 \
        #     or self.__lottery_numD4==self.__user_numD4 or self.__lottery_numD5==self.__user_numD5 :
        #
        #     print("ones of your numbers match the lottery. Your reward is $200!\n")



r=Lottery()
r.display_condition()
r.lottery_prize()