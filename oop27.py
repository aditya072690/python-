class Copy():
    def __int__(self):
        self.sfile=None
        self.tfile=None

    def display(self):
        self.sfile=input("Enter Source File's Name: ")
        try:
            filehandle = open(self.sfile, "r")
            self.tfile=input("Enter Target File's Name: ")
            texts = filehandle.readlines()
            filehandle.close()
            try:
                filehandle = open(self.tfile, "w")
                for s in texts:
                    filehandle.write(s)
                    filehandle.close()


                print("\nContent of \"" +self.sfile+ "\" gets Copied to \"" +self.tfile+ "\" Successfully!")
                print("\nWant to Display the Content of \"" +self.tfile+ "\" (y/n) ? ", end="")
                chk = input()
                if chk.islower()=='y':
                    try:
                        filehandle = open(self.tfile, "r")
                        contents = filehandle.readlines()
                        for s in contents:
                            print(s, end="")
                        filehandle.close()
                        print()
                    except IOError:
                        print("\nError occurred while opening the file!")

            except IOError:
                print("\nError occurred while opening/creating the file!")

        except IOError:
            print("\nThe file doesn't exist!")
r=Copy()
r.display()
