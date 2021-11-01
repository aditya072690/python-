import mysql.connector
import keyboard

class Candidate():

    def __init__(self):
        self.candidateData = {}  # {0:{"Name":"fgfsdg","contact" : 654465464, "Party's Name" : "AAP"},1:{"Name":"fgfsdg","contact" : 654465464}}
        self.__temp2 = 0
        self.__vote = 0


    def getInput(self):

        self.__mydb = mysql.connector.connect(host="localhost", user="root", password="Va1971-rshil", database="evm")
        self.__myc = self.__mydb.cursor()

        while True:
            self.__id = int(input("Enter Candidate's ID: "))
            if self.__id in self.candidateData.keys():
                print("The Candidate Id is not valid!!! It already exists.\n")
                continue
            else:
                if (self.__id == (self.__temp2 + 1)):
                    self.__temp2 += 1
                    break
                else:
                    print("Please maintain Candidate id sequence!!! Last Id used was: ", self.__temp2)
                    continue

        self.__name = input("Enter Candidate's Name :")
        self.__partyName = input("Enter Candidate's party name:")
        print("\n")
        #self.candidateData.update({self.__id: {"Name: ": self.__name, "Partys' Name: ": self.__partyName, "Vote(s): ": 0}})

        try:
            self.__myc.execute("Insert into candidates(id,name,partyname,votes)" + "values('" + str(self.__id) + "','" + self.__name + "','" + self.__partyName + "','" + str(self.__vote) + "')")
            self.__mydb.commit()
            print("Record Added Succesfully")
        except:
            self.__mydb.rollback()
            print("Failed!!!")
        self.__mydb.close()

    def addCandidates(self):
        for i in range(1, 5):
            self.getInput()

        while True:
            try:
                self.__temp = input('Do you want to add more candidates( Y(Yes) / N(NO) ): ')
            except:
                print("Numbers or Special characters are not allowed as lottery ticket number.")
                print("Please enter a valid input!!! (R'member for YES enter Y and for NO enter N).")
            else:
                if self.__temp == 'Y':
                    self.getInput()
                    print("A new candidate has been added!!!")
                    continue
                else:
                    break


class EVM(Candidate):
    def __init__(self):
        self.__mydb = mysql.connector.connect(host="localhost", user="root", password="Va1971-rshil", database="evm")
        self.__myc = self.__mydb.cursor()
        self.__myc.execute("SELECT id,partyname FROM evm.candidates")
        self.__temp = self.__myc.fetchall()
        self.__temp1 = []
        for i in range(len(self.__temp)):
            self.__temp1.append(int(self.__temp[i][0]))
        super().__init__()
        self.addCandidates()

    def getVote(self):
        print("Enter your votes: ")
        self.__mydb = mysql.connector.connect(host="localhost", user="root", password="Va1971-rshil", database="evm")
        self.__myc = self.__mydb.cursor()
        try:
            self.__myc.execute("SELECT id,partyname FROM evm.candidates")
            self.__temp = self.__myc.fetchall()
            for i,j in self.__temp:
                print('Press',i,'to vote',j)
        except:
            self.__mydb.rollback()
            print("Failed!!!")

        # for i in self.candidateData.keys():
        #     print('Please press', i, ' to vote', self.candidateData[i]["Partys' Name: "])
        print("\n")
        print("To exit voting, Please press Escape(Esc).")
        print("\n")
        while True:
            keyboard.read_key(suppress=False)
            try:
                self.__vote = keyboard.read_key()
                self.__vote = int(self.__vote)
            except:
                if self.__vote == 'esc':
                    #keyboard.release('esc')
                    break
                else:
                    print("Please press a number to vote!!!")
            else:
                #print(self.__temp[0][0])


                if self.__vote not in self.__temp1:
                    print("Please press a valid key!!!")
                    continue
                else:
                    try:

                        self.__myc.execute("update evm.candidates set votes=votes + 1 where id = '"+self.__vote+"'")
                        self.__mydb.commit()
                        #self.candidateData[self.__vote]["Vote(s): "] += 1
                        print("Your vote has been taken.")
                    except:
                        print("Something isn't right!!! Try Again")
                    continue

    def showVotes(self):
        print('\n\n Please press the id of the candidate, you want to see the result of: ')

        try:
            self.__myc.execute("SELECT id,partyname FROM evm.candidates")
            self.__temp = self.__myc.fetchall()
            for i, j in self.__temp:
                print('Press', i, 'for', j)
        except:
            self.__mydb.rollback()
            print("Failed!!!")

        print("\n")
        print("To exit, Please press Escape(Esc).")
        print("\n")

        while True:
            keyboard.read_key(suppress=False)
            try:
                self.__canIndex = keyboard.read_key()
            except:
                print("Please press a valid key!!!")
            else:
                if self.__canIndex == 'esc':
                    break
                else:
                    try:
                        self.__canIndex = int(self.__canIndex)
                    except:
                        print("Please press a valid key!!!")
                    else:
                        if self.__canIndex not in self.__temp1:
                            print("Please press a valid key!!! Entered key is out of range.")
                            continue
                        else:
                            try:
                                self.__myc.execute("SELECT name,partyname,votes FROM evm.candidates where id = '"+ str(self.__canIndex) +"'")
                                self.__temp = self.__myc.fetchall()

                            except:
                                self.__mydb.rollback()
                                print("Failed!!!")
                            else:
                                for j,k,l in self.__temp:
                                    print("# # # # # # # # # # # # # # # # # # # #")
                                    print("Id: ", self.__canIndex) #self.__canIndex)
                                    print("Name: ", j) #self.candidateData[self.__canIndex]["Name: "])
                                    print("Party Name: ", k) #self.candidateData[self.__canIndex]["Partys' Name: "])
                                    print("Vote(s): ", l) #self.candidateData[self.__canIndex]["Vote(s): "])
                                    print("# # # # # # # # # # # # # # # # # # # #")
                                    print("\n")
                                    continue



r = EVM()
r.getVote()
r.showVotes()