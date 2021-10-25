'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write a OOP program to input Customer id , Customer name, electricity unit charges used.
Calculate electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
'''

class ElectricityBill:

    def __init__(self):
        self.__cusid = 0
        self.__name = ''
        self.__unit_used = 0
        self.__tunit = 0

    def get_input(self):
        self.__cusid = int(input("Enter Customer  Id : "))
        self.__name = input("Enter Customer Name : ")
        self.__unit_used = int(input("Enter Customer Used Units : "))

    def calculate(self):
        self._extra = (self.__unit_used * 0.2 )

    def condition(self):
        unit = self.__unit_used

        if(unit <= 50):
            self.__tunit = unit*0.5
        elif(unit <= 100):
            self.__tunit = (50*0.5) + ((unit-50)*0.75)
        elif (unit <= 150):
            self.__tunit = (50*0.5) + (50*0.75) + ((unit-100) * 1.2)
        elif (unit <= 250):
            self.__tunit = (50*0.5) +(50*0.75)+(100*1.2)+((unit-150) * 1.5)
        elif (unit >= 250):
            self.__tunit = (50*0.5) + (50*0.75)+(100*1.2)+((unit - 150) * 2.3)


    def net_units(self):
        self._net_units = (self.__tunit + self._extra)


    def display(self):
        print("\n**************************************************************\n")
        print("Customer Id: ", self.__cusid)
        print("Customer Name: ", self.__name)
        print("Units Used  By the Costomer : ", self.__unit_used)
        print("Net Amount you want to pay : ", self._net_units)




run=ElectricityBill()
run.get_input()
run.calculate()
run.condition()
run.net_units()
run.display()