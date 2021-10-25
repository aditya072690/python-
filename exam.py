class Reduse:
    def __int__(self):
        self.num=0
        self.rem=0
    def input(self):

        self.num=int(input("enter a number :"))
        while(self.num/10 != 0):
            self.sum=0
            while(self.num!=0):
                self.rem=self.num%10
                self.sum+=self.rem
                self.num=self.num/10
            self.num=self.sum
        print(self.sum)
r=Reduse()
r.input()
# class SumofSum:
#     def _init_(self):
#         self.__main_digit = 0
#         self.__digit = 0
#         self.__e_digit = 0


#     def get_input(self):
#         self.__main_digit = int(input("Enter the Number :  "))


#     def Condition(self):

#         while (self.__main_digit / 10 != 0):

#             self.__digit = 0
#             while (self.__main_digit != 0):
#                     self.__e_digit = self.__main_digit % 10
#                     self.__digit += self.__e_digit
#                     self.__main_digit = self.__main_digit / 10
#             self.__main_digit = self.__digit

#     def display(self):
#         print("The number is :" , self.__digit)

# run=SumofSum()
# run.get_input()
# run.Condition()
# run.display()
# class SumofSum:
#     def _init_(self):
#         self.__main_digit = 0
#         self.__digit = 0
#         self.__e_digit = 0


#     def get_input(self):
#         self.__main_digit = int(input("Enter the Number :  "))


#     def Condition(self):

#         while (self.__main_digit / 10 != 0):

#             self.__digit = 0
#             while (self.__main_digit/10 != 0):
#                 while(self.__main_digit!=0):
#                     self.__e_digit = self.__main_digit % 10
#                     self.__digit += self.__e_digit
#                     self.__main_digit = self.__main_digit / 10
#             self.__main_digit = self.__digit

#     def display(self):
#         print("The number is :" , self.__digit)

# run=SumofSum()
# run.get_input()
# run.Condition()
# run.display()