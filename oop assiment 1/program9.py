'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write a program to display set of prime numbers between the given input range from user.
Enter start number : 10
Enter end number : 30
11,13,17,19,23,29
'''
class PrimeNumber:
    def __int__(self):
        self.Starting_Number=0
        self.Ending_Number=0
        self.num=0

    def display_Condition(self):
        self.Starting_Number=int(input("Enter Starting Number: "))
        self.Ending_Number=int(input("Enter Ending Number: "))
        lower_number = int(self.Starting_Number)
        upper_number = int(self.Ending_Number)
        print("\nPrime Numbers between the given range:")
        for self.num in range(lower_number, upper_number+1):
            if self.num>1:
                for i in range(2, self.num):
                    if(self.num%i)==0:
                        break
                else:
                    print(self.num)

r=PrimeNumber()
r.display_Condition()