import dataWriter
class RecordBuilder:
    def __init__(self):
        self.data = {'Name':'', 'Surname':'', 'Address':'', 'Age':'', 'Height':'', 'Salary':''}
        self.writer = dataWriter.DataWriter('output')

    def checkIfNew(self,nr):# check if quit

        return nr=='Y'

    def readFromKeyboard(self, message):
        return raw_input(message)


    def read(self):
        for p in self.data:
            x = self.readFromKeyboard(str(p)+": ")
            self.data[p]=x

        return self.data

    def readData(self):
        while True:
            x = self.readFromKeyboard('New record? (Y)')
            if self.checkIfNew(x):

                rk = self.read()
                self.writer.writeToFile(rk)
            else:
                break