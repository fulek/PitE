#Store data. Save to file and tar it if #entries == 10k. Also here read data and draw plots.
import tarfile
import os
import inputReaderValidator
class DataStore:
    def __init__(self,flightNumber):
        self.flightNumber=flightNumber

    def openNewFile(self, number):#open new file
        self.target = open(str(self.flightNumber)+"_"+str(int(number) )+".txt", 'w')

    def writeToFile(self,parameters):#write to file
        self.target.write(str(parameters))
        self.target.write("\n")

    def closeFile(self):#close file
        self.target.close()

    def targzFile(self):#tar gz file
        tar = tarfile.open(str(self.flightNumber)+".tar.gz", "w:gz")
        for name in self.findAlltextFile():
            tar.add(name)
        tar.close()
        self.removeTxt()

    def findAlltextFile(self):#find all text files
        files = []
        for file in os.listdir("./"):
            if file.endswith(".txt") and file.startswith(str(self.flightNumber)+"_"):
                files.append(file)
        return files

    def removeTxt(self):# remove all text files
        for file in self.findAlltextFile():
            os.remove(file)

    def unpackTargzFile(self):#unpack tar.gz file for readmode
        tar = tarfile.open(self.flightNumber+".tar.gz")
        tar.extractall()
        tar.close()
        print self.flightNumber+".tar.gz extracted in Current Directory"


    def readData(self):
        files = self.findAlltextFile()
        variables = []
        for file in files:
            with open(file) as fp:
                for line in fp:
                    try:
                        var = eval(line)
                        variables.append(var)
                    except (NameError, SyntaxError) as e:
                        print "Problem with line: "+line
                        print e

        return variables