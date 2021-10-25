'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write a program to check whether number is prime or not.
Enter a number : 13
13 is prime
Enter a number : 45
45 is not a prime number
'''

class Check :

    def __init__(self,number) :
        self.num = number

    def isPrime(self) :

        for i in range(2, int(num ** (1/2)) + 1) :

            if num % i == 0 :
                return False

        return True


num = 11
check_prime = Check(num)
print(check_prime.isPrime())
num = 14
check_prime = Check(num)
print(check_prime.isPrime())