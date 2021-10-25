'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write a OOP in python to input empid, name, basic salary, no. of experience in yrs. Calculate hra(35% of basic), da (58% of basic) and pf (9.5% of basic).
Also calculate bonus based on experience in years.
If experience in years is >= 30, bonus must be 59% of basic,
If experience in years is >=23, bonus must be 51% of basic,
If experience in years is >=15, bonus must be 45% of basic,
If experience in years is >=7, bonus must be 33% of basic,
If experience in years is <7, bonus must be 16% of basic
Calculate netsalary as basic+da+hra-pf+bonus.
'''

class Employee:
    def __init__(self):
        self.__empid = 0
        self.__name = ''
        self.__basic_sal = 0
        self.__experience = 0
    def get_input(self):


        while True:
            try:
                self.__empid = int(input('Please enter Employee Id: '))
                if (len(str(self.__empid)) != 8):
                    print('Please enter a valid Employee Id: ')
                    self.__empid = int(input('Please enter Employee Id: '))
                else:
                    pass
            except:
                print("Alphabets or Special characters are not allowed in Employee Id.")
            else:
                break


        self.__name = input('Please enter your name: ')

        while True:
            try:
                self.__basic_sal = int(input('Please enter your basic salary: '))
            except:
                print("Alphabets or Special characters are not allowed in Salary.")
            else:
                break

        while True:
            try:
                self.__experience = int(input('Please enter your experience: '))
            except:
                print("Alphabets or Special characters are not allowed in Salary.")
            else:
                break

    def calculate(self):
        self.__hra = (self.__basic_sal * 35) /100
        self.__da = (self.__basic_sal * 58) /100
        self.__pf = (self.__basic_sal * 9.5) /100

    def cal_bonus(self):
        exp = self.__experience
        self.__bonus = 0

        if exp >= 30:
            self.__bonus = 59
        elif exp >= 23:
            self.__bonus = 51
        elif exp >= 15:
            self.__bonus = 45
        elif exp >= 7:
            self.__bonus = 33
        elif exp < 7:
            self.__bonus = 16

        self.__calculated_bonus = (self.__basic_sal * self.__bonus) /100

    def net_salary(self):
        self.__netsalary = self.__basic_sal + self.__da + self.__hra - self.__pf + self.__calculated_bonus

    def display(self):
        print("\n")
        print("Employee Id: ",self.__empid)
        print("Name: ",self.__name)
        print("Basic salary: ",self.__basic_sal)
        print("No. of Experience: ",self.__experience)
        print("HRA: ",self.__hra)
        print("DA: ",self.__da)
        print("PF: ",self.__pf)
        print("Bonus: ",self.__calculated_bonus)
        print("Net Salary: ",self.__netsalary)
run = Employee()
run.get_input()
run.calculate()
run.cal_bonus()
run.net_salary()
run.display()