# Q. Write an OOP program with list of 5 elements.
# Add a function in class to sort the elements in ascending / descending order.
# def mysort(numlist, order):  order=asc or desc
# # By default if you only pass list of numbers, it will always sort in ascending order.
class List():
    def __init__(self):
        self.__list = []
        self.__size = int(input("Please enter the Total Number of List Elements: "))

    def getInput(self):
        for i in range(1, self.__size + 1):
            self.__value = int(input("Please enter the Value of %d Element : " % i))
            self.__list.append(self.__value)

        self.__order = input("Please enter the order[Ascending(asc)/Descending(dsc)]: ")

    def sortList(self):
        if self.__order == 'Asc' or self.__order == 'asc' or self.__order == 'ASC':
            for i in range(self.__size):
                for j in range(i + 1, self.__size):
                    if self.__list[i] > self.__list[j]:
                        self.__temp = self.__list[i]
                        self.__list[i] = self.__list[j]
                        self.__list[j] = self.__temp
            print("Elements After Sorting List in Ascending Order is : ", self.__list)

        elif self.__order == 'Dsc' or self.__order == 'dsc' or self.__order == 'DSC':
            for i in range(self.__size):
                for j in range(i + 1, self.__size):
                    if self.__list[i] < self.__list[j]:
                        self.__temp = self.__list[i]
                        self.__list[i] = self.__list[j]
                        self.__list[j] = self.__temp
            print("Elements After Sorting List in Descending Order is : ", self.__list)

        else:
            print("Wrong Input!!!!!")
            self.__order = input("Please enter the order[Ascending(asc)/Descending(dsc)]: ")
            self.sortList()

r = List()
r.getInput()
r.sortList()
