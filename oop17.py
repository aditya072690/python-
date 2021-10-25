class BankAccount:

    def __init__(self):
        self.ID=0
        self.Name=''
        self.BankName=''
        self.__input = 0
        self.__transaction = 0
        self.balance = 50000

    def display_Condition(self):

        self.BankName=input("Enter Your Bank Name: ")
        print("Bank of ",self.BankName)

        self.Name=(input("Enter Your Name:"))
        print("Account Holder Name: ",self.Name)

        self.ID = int(input('Enrollment id: '))
        while (len(str(self.ID)) != 8):
                print('Plese enter a valid Enrolment Id: ')
                id = int(input('Enrollment id: \n'))
        print("Account number: ",self.ID)

        print("\nChoose your service from below option (Enter your choice)")
        print("Enter 1 to Choose Saving Account ")
        print("Enter 2 to Choose fixed Deposit")
        self.__input = int(input("enter a choose: "))

        if (self.__input == 1):
            print("You choose Saving Account")
            print("Enter your transaction type")
            print("Enter 1 to Choose Withdrawal Amout")
            print("Enter 2 to Deposit")
            self.__transaction = int(input("Enter Your Choice :"))
            if (self.__transaction == 1):
                print("You Choose Withdrawal :")
                FixedDeposit.withdraw(self)
                FixedDeposit.display(self)
            else:
                print("You Chosse Deposit  ")
                FixedDeposit.deposit(self)
                FixedDeposit.display(self)
        else:
            print("You choose fixed Deposit ")
            FixedDeposit.interest(self)

        #print("your balance is : ", self.balance)





class SavingAccount:

    def __init__(self):
        self.balance = 50000

    def deposit(self):
        self.amount = float(input("Enter amount to be Deposited: "))
        self.balance += self.amount
        print("\n Amount Deposited:", self.amount)

    def withdraw(self):
        self.amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= self.amount:
            self.balance -= self.amount
            print("\n You Withdrew:", self.amount)
        else:
            print("\n Insufficient balance ")

    def fixed_deposit(self):
        self.principal = int(input(''))

    def display(self):
        print("\n Net Available Balance=", self.balance)

class FixedDeposit(SavingAccount,BankAccount):

    def __init__(self):
        super().__init__()
        self.amount = 0
        self.rate = 6.7
        self.years = 0
        self.profit = 0
    def interest(self):
        self.amount = int(input('Enter Principal Amount: '))
        self.years = int(input('Enter no. of years: '))
        self.profit = (self.amount * (1 + (self.rate/100)) ** self.years)
        print("The bank ratecurrently {0}%, you will receive {1} after {2} years.".format(self.rate,self.profit,self.years))

r = FixedDeposit()
r.display_Condition()
boolean = True
while boolean:
    u_input = input('Do you wish to continue(y/n):')
    if u_input == 'y':
        r = FixedDeposit()
        r.display_Condition()
    else:
        boolean = False
# r.deposit()
# r.withdraw()
# r.display()