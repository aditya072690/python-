class exponent:
    def findFact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f

print("Enter a Number: ", end="")
num = int(input())

ob = exponent()
print("\nFactorial of", num, "=", ob.findFact(num))