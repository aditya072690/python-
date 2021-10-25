class PrimeNumber:
    def __int__(self):
        self.Starting_Number=0
        self.Ending_Number=0
        self.num=0

    def display_Condition(self):
        # print("Enter Staring Number: ")
        self.Starting_Number=int(input("Enter Staring Number: "))
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