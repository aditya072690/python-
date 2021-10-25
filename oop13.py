class Calculator:
    def _init_(self):
        self.__num_1 = int(input('Please enter number 1: '))
        self.__operator = input('Please enter mathematical operator: ')
        self.__num_2 = int(input('Please enter number 2: '))

    def calculate(self):
        self.calculation = 0
        self.__opName = ''
        if self.__operator == '+':
            self.calculation = self.__num_1 + self.__num_2
            self.__opName = 'Addition'
        elif self.__operator == '-':
            self.__calculation = self.__num_1 - self.__num_2
            self.__opName = 'Subtraction'
        elif self.__operator == '*':
            self.__calculation = self.__num_1 * self.__num_2
            self.__opName = 'Multiplication'
        elif self.__operator == '/':
            self.__calculation = self.__num_1 / self.__num_2
            self.__opName = 'Division'

    def display(self):
        print('The {0} of {1} and {2} is {3}.'.format(self.__opName,self.__num_1,self.__num_2,self.__calculation))

run =Calculator()
run.calculate()
run.display()