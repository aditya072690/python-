# Write an OOP program to accept two numbers and one mathematical operator. Calculate and display appropriate answer.
#
# Eg output
# Enter first number : 45
# Enter mathematical operator : +
# Enter second number : 60
# 45 + 60 = 105
# Note : Make use of Operator overloading concept
# In python Operator overloading is accomplished by following operator mapped functions
# +: __add__  , *: __mul__ , /: __truediv__ ,    -: __sub__
# //: __floordiv__ ,  %: __mod__   , **: __pow__ ,
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
    # def __sub__(self, ):

n1 = Mynumber(10)
n2 = Mynumber()
n2.set_no(30)

print()
n1.display()
print()
n2.display()
print()

n3=n1+n2
print("Addition of to number is ", n3.get_no())
