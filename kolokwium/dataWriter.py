class DataWriter:
    def __init__(self, fileName):
        self.FileName = fileName

    def writeToFile(self, data):
        f = open(self.FileName+'.txt', 'a')
        f.write(str(data))
        f.write("\n")
        f.close()

    def checkIfFloat(self,x):#check if number is float
            try:
                float(x)
                return True
            except ValueError:
                pass

    def readNamesAndGrades(self):
        namesAndGrades = []
        with open(self.FileName) as fp:
            for line in fp:
                namesAndGrades.append(line)

        return namesAndGrades
