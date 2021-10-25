class Employee:
    def _init_(self):
        self.__empid = 0
        self.__name = ''
        self.__basic_sal = 0
        self.__experience = 0
    def get_input(self):
        self.__empid = int(input('Please enter employee id: '))
        self.__name = input('Please enter your name: ')
        self.__basic_sal = int(input('Please enter your basic salary: '))
        self.__experience = int(input('Please enter your experience: '))
    def calculate(self):
        self._hra = (self.__basic_sal * 35) /100
        self._da = (self.__basic_sal * 58) /100
        self._pf = (self.__basic_sal * 9.5) /100

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

        self._calculated_bonus = (self.__basic_sal * self.__bonus) /100

    def net_salary(self):
        self._netsalary = self.__basic_sal + self._da + self._hra - self._pf + self._calculated_bonus

    def display(self):
        print("\n")
        print("Employee Id: ",self.__empid)
        print("Name: ",self.__name)
        print("Basic salary: ",self.__basic_sal)
        print("No. of Experience: ",self.__experience)
        print("HRA: ",self._hra)
        print("DA: ",self._da)
        print("PF: ",self._pf)
        print("Bonus: ",self._calculated_bonus)
        print("Net Salary: ",self._netsalary)
run = Employee()
run.get_input()
run.calculate()
run.cal_bonus()
run.net_salary()
run.display()