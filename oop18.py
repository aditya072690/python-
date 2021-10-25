class Mynumber:

    def __init__(self,no=0):
        self.__no = no

    # get no
    def get_no(self):
        return self.__no

    # set no
    def set_no(self, no):
        self.__no = no

    def display(self):
        print("The value of rno is ", self.__no)

    def add(self, tn2):
        tnum = Mynumber()
        tnum.__no = self.__no + tn2.__no
        return tnum

    def __add__(self, tn2):  # + -> __add__, *-> __mul__, - -> __sub__ , > -> __gt__ , >= -> __ge__
        tnum = Mynumber()
        tnum.__no = self.__no + tn2.__no
        return tnum

    def __sub__(self, tn2):
        tnum = Mynumber()
        tnum.__no = self.__no - tn2.__no
        return tnum

    def __mul__(self, tn2):
        tnum = Mynumber()
        tnum.__no = self.__no * tn2.__no
        return tnum

    def __gt__(self, tn2):
        if self.__no > tn2.__no:
            print("The number {0} is greater than {1}.".format(self.__no, tn2.__no))
        else:
            print("The number {0} is greater than {1}.".format(tn2.__no,self.__no))


n1 = Mynumber(10)
n2 = Mynumber()
n2.set_no(30)

print()
n1.display()
print()
n2.display()
print()

n3 = n1 + n2


n4 = n1 - n2


n5 = n1 * n2




print("Addition of to number is ", n3.get_no())
print("Subtraction of to number is ", n4.get_no())
print("Multiplication of to number is ", n4.get_no())
n6 = n1 > n2