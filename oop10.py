class exponent:

    def __init__(self, num, pow, result):
        self.num = num
        self.pow = pow
        self.result = result

    def __str__(self):
        return "For Base {0} and Power {1} , the Answer is {2}".format(self.num,self.pow,self.result)

    def value(self):
        solution = self.num ** self.pow
        return exponent(self.num,self.pow,solution)

base = int(input('Enter Base Value: '))
pow = int(input('Enter Power of  Value: '))

a = exponent(base, pow, 1)
print(a.value())