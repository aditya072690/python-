
# Write an Object Oriented Program which reads texts  from a file. It must display file statistics a below.
# No. of sentences.
# No. of words.
# No. of total characters (Does not include whitespace)
# No. of whitespaces
# Total no. of digits, uppercase and lowercase letters
import sys
class File():
    def __int__(self):
        pass
    def Sentences(self):
        self.__file = open("File.txt", "r")
        self.__Count = 0
        self.__Content = self.__file.read()
        self.__data = self.__Content.split(".")
        for i in self.__data:
            if i:
                self.__Count += 1
        print("The number of lines  is : ",self.__Count)
        print("\n")

    def Word(self):
        self.__file = open("File.txt", "rt")
        self.__data = self.__file.read()
        self.__Words = self.__data.split()
        print('Number of words is :', len(self.__Words))
        print("\n")

    def TotalCharacters(self):
        self.__file = open("File.txt", "r")
        self.__data = self.__file.read().replace(" ","")
        self.__TotalNumberCharacters = len(self.__data)
        print('Number of characters is :', self.__TotalNumberCharacters)
        print("\n")

    def Whitespaces(self):
        self.__count = 0
        self.__file = open("File.txt",'rt')
        self.__data=self.__file.read()
        self.__data.split()
        for i in self.__data:
            if(i.isspace()):
                self.__count =self.__count+1
        print("The number of Whitespaces is: ",self.__count)

    def DigitsUppercaseLowercase(self):
        self.__uppercase_letters=0
        self.__lowercase_letters=0
        self.__file = open("file.txt")
        self.__data = self.__file.read()
        for letters in self.__data:
            if letters >= 'A' and letters <= 'Z':
                self.__uppercase_letters += 1
            elif letters >= 'a' and letters <= 'z':
                self.__lowercase_letters += 1
        self.__digits = 0
        for content in self.__data:
            if content.isdigit() == True:
                self.__digits += 1

        print('Lower case letters= ',self.__lowercase_letters)
        print('Upper case letters= ',self.__uppercase_letters)
        print("No of Digits is :  ",self.__digits)
r=File()
while True:
    print("Display File Statistics")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.No. Of Sentences")
    print("2.No.  Of Words")
    print("3.No. Of Total Characters (Dose not inlucde whitespace)")
    print("4.No. of Whitespace")
    print("5.Total no. of digits,uppercase and lowercase letters")
    print("6.exit")
    chioce=int(input("enter youer chioce: "))
    if chioce==1:
        r.Sentences()
    elif chioce==2:
        r.Word()
    elif chioce==3:
        r.TotalCharacters()
    elif chioce==4:
        r.Whitespaces()
    elif chioce==5:
        r.DigitsUppercaseLowercase()
    elif chioce==6:
        sys.exit()