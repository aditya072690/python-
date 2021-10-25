# n=int(input("Enter number:"))
# t=n
# rev=0
# while(n>0):
#     dig=n%10# Finding the remainder
#     rev=rev*10+dig
#     n=n//10# Finding the quotient
# if(t==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")
class Palindrome:
    def __int__(self):
        self.Number=0
        self.rev=0
        self.dig=0
        self.t=0
    def display_Condition(self):
        self.rev=0
        self.Number=int(input("Enter number:"))
        self.t=self.Number
        while(self.Number>0):
            self.dig=self.Number%10# Finding the remainder
            self.rev=self.rev*10 + self.dig
            self.Number=self.Number//10# Finding the quotient
        if(self.t==self.rev):
            print("The number is a palindrome!")
        else:
            print("The number isn't a palindrome!")

r=Palindrome()
r.display_Condition()
