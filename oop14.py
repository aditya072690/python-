class Electricity_Bill:
    def _init_(self):
        self.customer_id=0
        self.customer_name=''
        self.electricity_unit=0

    def get_input(self):
        self.customer_id = int(input("Enter Customer  Id : "))
        self.customer_name = int(input("Enter Customer Name : "))
        self.electricity_unit = int(input("Enter electricity unit : "))

    def calculate(self):
        self._price = 350
        self.extra = (self.electricity_unit * 20 )/100

    def condition(self):
        unit = self.electricity_unit
        self.__un = 0

        if unit >= 251
            self.__un = 2.5
        elif unit < 251
            self.__un = 1.5
        elif unit < 151
            self.__un = 1.2
        elif unit < 101
            self.__un = 0.75
        elif unit < 51
            self.__un = 0.5

        self._calculated_units(self._price * self._unit)

    def net_units(self):
        self._net_units = (self._calculated_units + self._extra)

    def display(self):
        print("\n")
        print("customer Id: ",self.customer_id)
        print("customer Name: ",self.customer_name)
        print("ele: ",self.electricity_unit)
