import keyboard


class Candidate():
    def __init__(self):
        self.candidateData = {}
        self.__temp2 = 0

    def getInput(self):

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
                    print(
                        "Please maintain Candidate id sequence!!! Last Id used was: ", self.__temp2)
                    continue

        self.__name = input("Enter Candidate's Name :")
        self.__partyName = input("Enter Candidate's party name:")
        print("\n")
        self.candidateData.update({self.__id: {
            "Name: ": self.__name, "Partys' Name: ": self.__partyName, "Vote(s): ": 0}})
        #self.candidateData = sorted(self.candidateData)
        # print(self.candidateData.keys())

    def addCandidates(self):
        for i in range(1, 5):
            self.getInput()

        while True:
            try:
                self.__temp = input(
                    'Do you want to add more candidates( Y(Yes) / N(NO) ): ')
            except:
                print(
                    "Numbers or Special characters are not allowed as lottery ticket number.")
                print(
                    "Please enter a valid input!!! (R'member for YES enter Y and for NO enter N).")
            else:
                if self.__temp == 'Y':
                    self.getInput()
                    print("A new candidate has been added!!!")
                    continue
                else:
                    break


class EVM():
    def __init__(self):
        self.__candidate = Candidate()
        self.__candidate.addCandidates()

    def getVote(self):
        print("Enter your votes: ")
        for i in self.__candidate.candidateData.keys():
            print('Please enter', i, ' to vote',
                  self.__candidate.candidateData[i]["Partys' Name: "])
        while True:

            try:
                if keyboard.is_pressed('esc'):
                    break
                self.__vote = int(input())
                self.__candidate.candidateData[self.__vote]["Vote(s): "] += 1
            except:
                break
            else:
                continue

    def showVotes(self):
        print('Please enter the id of the candidate, you want to see the result of: ')

        for i in self.__candidate.candidateData.keys():
            print('Please enter', i, 'for',
                  self.__candidate.candidateData[i]["Partys' Name: "])

        self.__canIndex = int(input())

        print("# # # # # # # # # # # # # # # # # # # #")
        print("Id: ", self.__canIndex)
        print(
            "Name: ", self.__candidate.candidateData[self.__canIndex]["Name: "])
        print("Party Name: ",
              self.__candidate.candidateData[self.__canIndex]["Partys' Name: "])
        print("Vote(s): ",
              self.__candidate.candidateData[self.__canIndex]["Vote(s): "])
        print("# # # # # # # # # # # # # # # # # # # #")


r = EVM()
r.getVote()
r.showVotes()
