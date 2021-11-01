''' Using Pickle library, write an object oriented program to perform CRUD operations on products object.
Create a class which encapsulates Product information such as productId, productName and productPrice.
Store its object collection using dictionary to a file making use of Pickle library.'''
# Program for pickling python lists
# importing module
# print('<-------------------Pickling----------------------->')
# import pickle
# # number of input data to take
# n = int(input("Enter the number of items "))
# data = []  # input list
# # adding items to the list
# for d in range(n):
#     item = input("Enter data :" + str(d+1)+': ')
# data.append((item))
# # open a file where data need to be stored
# file = open('list.pkl', 'wb')
# # dump information to the file
# pickle.dump(data, file)
# # close the file
# file.close()
# print('\n')
# print('<-------------------Un-Pickling----------------------->')
# # open the file where data is dumped
# fileo = open('list.pkl', 'rb')
# # loading data
# datao = pickle.load(fileo)
# # close the file
# fileo.close()
# # showing pickled data
# print("showing data pickled")
# for i in datao:
#     print(i)
#
#
import pickle
class Product():
    def __int__(self):
        self.__productId=None
        self.__productName=None
        self.__productPrice=None
        self.__file=None

    def input(self):
        self.__productId=int(input("Enter Your Product ID :"))
        self.__productName=input("Enter you Product Name:")
        self.__productPrice=int(input("Enter you Product Price:"))

        self.__Data={"ProductId":self.__productId,"ProductName":self.__productName,"ProductPrice":self.__productPrice}
        self.data=str(self.__productId)+".txt"
        self.__file=open(self.data,'wb')
        pickle.dump(self.__Data,self.__file)
        self.__file.close()
        print("\n")
        print("---------------------------------------------------")
        self.datao=str(self.__productId)+".txt"
        self.__fileo=open(self.datao,"rb")
        self.__Data=pickle.load(self.__fileo)
        print("showing data pickled")
        for i,k in self.__Data.items():
            print(i,"---",k)
        self.__fileo.close()

r=Product()
r.input()