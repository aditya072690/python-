# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#             d["UPPER_CASE"]+=1
#         elif c.islower():
#             d["LOWER_CASE"]+=1
#         else:
#             pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
#
# string_test('The quick Brown Fox')
#
# # Python 3 program to count the uppercase,
# # lowercase, special characters
# # and numeric values
#
# # Function to count uppercase, lowercase,
# # special characters and numbers
# def Count(str):
#     upper, lower, number, special = 0, 0, 0, 0
#     for i in range(len(str)):
#         if str[i].isupper():
#             upper += 1
#         elif str[i].islower():
#             lower += 1
#         elif str[i].isdigit():
#             number += 1
#         else:
#             special += 1
#     print('Upper case letters:', upper)
#     print('Lower case letters:', lower)
#     print('Number:', number)
#     print('Special characters:', special)
#
# # Driver Code
# str = "#GeeKs01fOr@gEEks07"
# Count(str)
#
# # This code is contributed
# # by Sushma Reddy
#
# def main():
#
#     uppercase_count = 0
#     lowercase_count = 0
#     digits_count = 0
#     whitespace_count = 0
#
#     uppercase =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     digits = ['0','1','2','3','4','5','6','7','8','9']
#     whitespace = [' ']
#
#     infile = open("text.txt", "r")
#
#     data = infile.readlines()
#
#     for character in data:
#         if character in uppercase:
#             uppercase_count += 1
#
#     for character in data:
#         if character in lowercase:
#             lowercase_count += 1
#
#     for character in data:
#         if character in digits:
#             digits_count += 1
#
#     for character in data:
#         if character in whitespace:
#             whitespace_count += 1
#
#     print('The uppercase count is',uppercase_count)
#     print('The lowercase count is',lowercase_count)
#     print('The digit count is',digits_count)
#     print('The whitespace count is',whitespace_count)
#
# main()
# # ___________
# count = 0;
#
# #Opens a file in read mode
# file = open("data.txt", "r")
#
# #Gets each line till end of file is reached
# for line in file:
#     #Splits each line into words
#     words = line.split(" ");
#     #Counts each word
#     count = count + len(words);
#
# print("Number of words present in given file: " + str(count));
# file.close();
# # ------------
# # Python implementation to compute
# # number of characters, words, spaces
# # and lines in a file
#
# # Function to count number
# # of characters, words, spaces
# # and lines in a file
# def counter(fname):
#
#     # variable to store total word count
#     num_words = 0
#
#     # variable to store total line count
#     num_lines = 0
#
#     # variable to store total character count
#     num_charc = 0
#
#     # variable to store total space count
#     num_spaces = 0
#
#     # opening file using with() method
#     # so that file gets closed
#     # after completion of work
#     with open(fname, 'r') as f:
#
#         # loop to iterate file
#         # line by line
#         for line in f:
#
#             # incrementing value of
#             # num_lines with each
#             # iteration of loop to
#             # store total line count
#             num_lines += 1
#
#             # declaring a variable word
#             # and assigning its value as Y
#             # because every file is
#             # supposed to start with
#             # a word or a character
#             word = 'Y'
#
#             # loop to iterate every
#             # line letter by letter
#             for letter in line:
#
#                 # condition to check
#                 # that the encountered character
#                 # is not white space and a word
#                 if (letter != ' ' and word == 'Y'):
#
#                     # incrementing the word
#                     # count by 1
#                     num_words += 1
#
#                     # assigning value N to
#                     # variable word because until
#                     # space will not encounter
#                     # a word can not be completed
#                     word = 'N'
#
#                 # condition to check
#                 # that the encountered character
#                 # is a white space
#                 elif (letter == ' '):
#
#                     # incrementing the space
#                     # count by 1
#                     num_spaces += 1
#
#                     # assigning value Y to
#                     # variable word because after
#                     # white space a word
#                     # is supposed to occur
#                     word = 'Y'
#
#                 # loop to iterate every
#                 # letter character by
#                 # character
#                 for i in letter:
#
#                     # condition to check
#                     # that the encountered character
#                     # is not white space and not
#                     # a newline character
#                     if(i !=" " and i !="\n"):
#
#                         # incrementing character
#                         # count by 1
#                         num_charc += 1
#
#     # printing total word count
#     print("Number of words in text file: ", num_words)
#
#     # printing total line count
#     print("Number of lines in text file: ", num_lines)
#
#     # printing total character count
#     print('Number of characters in text file: ', num_charc)
#
#     # printing total space count
#     print('Number of spaces in text file: ', num_spaces)
#
# # Driver Code:
# if __name__ == '__main__':
#     fname = 'File1.txt'
#     try:
#         counter(fname)
#     except:
#         print('File not found')
#
# class File():
#     def TotalCharacters(self):
#         self.__file = open("File.txt", "r")
#         self._Content = self.__file.read()
#         self._data = self._Content.split("\n")
#         sum = 0
#         for i in range(self._data):
#             sum = sum+1
#
#         print("\nTotal Characters = " + str(sum))
# r=File()
# r.TotalCharacters()
#
# def DigitsUppercaseLowercase(self):
#     print("Enter the String: ", end="")
#     text = input()
#     textLen = len(text)
#     sum = 0
#     for i in range(textLen):
#         if text[i]>='A' and text[i]<='Z':
#             sum = sum+1
#
#     print("\nUppercase Characters = " + str(sum))
#
#     print(end="Enter the String: ")
#     text = input()
#     textLen = len(text)
#     sum = 0
#     for i in range(textLen):
#         if text[i]>='a' and text[i]<='z':
#             sum = sum+1
#
#     print("\nLowercase Characters = " + str(sum))
#
#     string=input("Enter string:")
#     count1=0
#     for i in string:
#         if(i.isdigit()):
#             count1=count1+1
#     print("The number of digits is:")
#     print(count1)


class File():
    def __init__(self):
        self.__file = None
        self.__sentences = 0
        self.__white_spaces = 0
        self.__characters = 0
        self.__words = 0
        self.__digits = 0
        self.__uppercase_letters = 0
        self.__lowercase_letters = 0

    def readFile(self):
        self.__file = open("file.txt","r")
        self.__file = self.__file.read()
        self.__sentences = self.__file.count(".")
        self.__words = len(self.__file.split())
        self.__characters = len(self.__file) - self.__file.count(" ")
        self.__white_spaces = self.__file.count(" ")
        for content in self.__file:
            if content.isdigit() == True:
                self.__digits += 1
        for letters in self.__file:
            if letters >= 'A' and letters <= 'Z':
                self.__uppercase_letters += 1
            elif letters >= 'a' and letters <= 'z':
                self.__lowercase_letters += 1
    def display(self):
        print("Sentences: ",self.__sentences)
        print("Words: ",self.__words)
        print("Characters: ",self.__characters)
        print("White Spaces: ",self.__white_spaces)
        print("Digits: ",self.__digits)
        print("Uppercase Letters: ",self.__uppercase_letters)
        print("Lowercase letters: ",self.__lowercase_letters)
r = File()
r.readFile()
r.display()